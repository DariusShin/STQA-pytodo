"""Selenium page helpers (a light Page Object layer) for PyTodo Pro.

Tests describe *what* a user does ("create a task", "filter by Work"); the
locators and waits live here, so a markup change is fixed in one place rather
than in every test. Every action is logged to the run's pytest.log.
"""

import logging
from urllib.parse import urlparse

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

log = logging.getLogger("w6.ui")

TIMEOUT = 10

ROWS = (By.CSS_SELECTOR, "table.task-table tbody tr")
EMPTY_ROW = (By.CSS_SELECTOR, "table.task-table td.empty")


class PyTodoUI:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url.rstrip("/")

    # -- navigation and page state -------------------------------------------

    def open(self, path):
        log.info("UI open %s", path)
        self.driver.get(self.base_url + path)

    @property
    def path(self):
        return urlparse(self.driver.current_url).path

    def heading(self):
        return self.driver.find_element(By.TAG_NAME, "h1").text.strip()

    def error_text(self):
        found = self.driver.find_elements(By.CSS_SELECTOR, "p.error")
        return found[0].text.strip() if found else None

    def nav_username(self):
        found = self.driver.find_elements(By.CSS_SELECTOR, "nav .nav-user")
        return found[0].text.strip() if found else None

    def _click_and_wait_for_load(self, element):
        """Click something that submits/navigates and wait for the new document."""
        old_root = self.driver.find_element(By.TAG_NAME, "html")
        element.click()
        WebDriverWait(self.driver, TIMEOUT).until(EC.staleness_of(old_root))

    def _field(self, name):
        return self.driver.find_element(By.NAME, name)

    def validation_state(self, name):
        """The browser's constraint-validation state for a form field."""
        return self.driver.execute_script(
            "const el = arguments[0];"
            "return {valueMissing: el.validity.valueMissing, valid: el.validity.valid,"
            "        message: el.validationMessage};",
            self._field(name),
        )

    # -- authentication --------------------------------------------------------

    def _fill_credentials(self, username, password):
        user, pw = self._field("username"), self._field("password")
        user.clear()
        pw.clear()
        if username:
            user.send_keys(username)
        if password:
            pw.send_keys(password)

    def submit_form(self, wait=True):
        button = self.driver.find_element(By.CSS_SELECTOR, "form button[type=submit]")
        if wait:
            self._click_and_wait_for_load(button)
        else:
            button.click()  # e.g. blocked by native required-field validation

    def submit_form_if_accepted(self, timeout=3):
        """Submit when either outcome is legitimate: the page may navigate (input
        accepted) or stay put (input rejected client-side). Returns True if it navigated."""
        button = self.driver.find_element(By.CSS_SELECTOR, "form button[type=submit]")
        old_root = self.driver.find_element(By.TAG_NAME, "html")
        button.click()
        try:
            WebDriverWait(self.driver, timeout).until(EC.staleness_of(old_root))
            return True
        except TimeoutException:
            return False

    def register(self, username, password, wait=True):
        log.info("UI register username=%r (len %d), password len %d",
                 username, len(username or ""), len(password or ""))
        self.open("/register")
        self._fill_credentials(username, password)
        self.submit_form(wait=wait)

    def login(self, username, password):
        log.info("UI login username=%r", username)
        self.open("/login")
        self._fill_credentials(username, password)
        self.submit_form()

    def logout(self):
        log.info("UI logout via navigation bar")
        link = self.driver.find_element(By.LINK_TEXT, "Log out")
        self._click_and_wait_for_load(link)

    # -- task form -------------------------------------------------------------

    def fill_task_form(self, title=None, description=None, category=None, due_date=None):
        if title is not None:
            field = self._field("title")
            field.clear()
            field.send_keys(title)
        if description is not None:
            field = self._field("description")
            field.clear()
            field.send_keys(description)
        if category is not None:
            Select(self._field("category_id")).select_by_visible_text(category or "None")
        if due_date is not None:
            # Date inputs are locale-dependent when typed, so set the ISO value directly
            # and fire the events a real edit would (limitation recorded in the README).
            self.driver.execute_script(
                "arguments[0].value = arguments[1];"
                "arguments[0].dispatchEvent(new Event('input', {bubbles: true}));"
                "arguments[0].dispatchEvent(new Event('change', {bubbles: true}));",
                self._field("due_date"), due_date or "",
            )

    def create_task(self, title, description=None, category=None, due_date=None, wait=True):
        log.info("UI create task title=%r category=%r due=%r", title, category, due_date)
        self.open("/tasks/new")
        self.fill_task_form(title, description, category, due_date)
        self.submit_form(wait=wait)

    def task_form_values(self):
        return {
            "title": self._field("title").get_attribute("value"),
            "description": self._field("description").get_attribute("value"),
            "category": Select(self._field("category_id")).first_selected_option.text.strip(),
            "due_date": self._field("due_date").get_attribute("value"),
        }

    def cancel_task_form(self):
        log.info("UI cancel task form")
        self._click_and_wait_for_load(self.driver.find_element(By.LINK_TEXT, "Cancel"))

    # -- task list -------------------------------------------------------------

    def rows(self):
        """Visible task rows as dictionaries (the empty-state row is excluded)."""
        result = []
        for tr in self.driver.find_elements(*ROWS):
            cells = tr.find_elements(By.TAG_NAME, "td")
            if len(cells) < 6:
                continue
            result.append({
                "title": cells[1].text.strip(),
                "category": cells[2].text.strip(),
                "due_date": cells[3].text.strip(),
                "urgency": cells[4].text.strip(),
                "toggle": cells[0].text.strip(),
                "done": "done" in (tr.get_attribute("class") or "").split(),
                "element": tr,
            })
        return result

    def titles(self):
        return [r["title"] for r in self.rows()]

    def row(self, title):
        matches = [r for r in self.rows() if r["title"] == title]
        if not matches:
            raise NoSuchElementException(f"no task row titled {title!r}; visible: {self.titles()}")
        return matches[0]

    def empty_message(self):
        found = self.driver.find_elements(*EMPTY_ROW)
        return found[0].text.strip() if found else None

    def toggle(self, title):
        log.info("UI toggle complete/reopen for %r", title)
        button = self.row(title)["element"].find_element(By.CSS_SELECTOR, "button.check-btn")
        self._click_and_wait_for_load(button)

    def open_edit(self, title):
        log.info("UI open edit form for %r", title)
        link = self.row(title)["element"].find_element(By.LINK_TEXT, "Edit")
        self._click_and_wait_for_load(link)

    def delete(self, title, confirm):
        """Click Delete and answer the native confirm() dialog. Returns the dialog text."""
        log.info("UI delete %r, confirm=%s", title, confirm)
        button = self.row(title)["element"].find_element(By.CSS_SELECTOR, "button.link-btn")
        old_root = self.driver.find_element(By.TAG_NAME, "html")
        button.click()
        alert = WebDriverWait(self.driver, TIMEOUT).until(EC.alert_is_present())
        text = alert.text
        if confirm:
            alert.accept()
            WebDriverWait(self.driver, TIMEOUT).until(EC.staleness_of(old_root))
        else:
            alert.dismiss()
        return text

    # -- filters ---------------------------------------------------------------

    def filter_category(self, name):
        log.info("UI filter category=%r", name)
        select = Select(self._field("category"))
        old_root = self.driver.find_element(By.TAG_NAME, "html")
        select.select_by_visible_text(name)  # onchange submits the form
        WebDriverWait(self.driver, TIMEOUT).until(EC.staleness_of(old_root))

    def filter_status(self, label):
        log.info("UI filter status=%r", label)
        select = Select(self._field("status"))
        old_root = self.driver.find_element(By.TAG_NAME, "html")
        select.select_by_visible_text(label)
        WebDriverWait(self.driver, TIMEOUT).until(EC.staleness_of(old_root))

    def search(self, text):
        log.info("UI search q=%r", text)
        field = self._field("q")
        field.clear()
        field.send_keys(text)
        button = self.driver.find_element(By.CSS_SELECTOR, "form.filters button[type=submit]")
        self._click_and_wait_for_load(button)

    # -- dashboard -------------------------------------------------------------

    def dashboard_counters(self):
        self.open("/dashboard")
        counters = {}
        for card in self.driver.find_elements(By.CSS_SELECTOR, ".stat-card"):
            label = card.find_element(By.CSS_SELECTOR, ".stat-label").text.strip()
            counters[label] = int(card.find_element(By.CSS_SELECTOR, ".stat-value").text.strip())
        log.info("UI dashboard counters %s", counters)
        return counters
