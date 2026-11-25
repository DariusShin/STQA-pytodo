"""
Week 5 shared settings, matched to PyTodo Pro (pytodo_pro_student, app.py).
Only BASE_URL should need changing, e.g. if you run on another port.
"""

BASE_URL = "http://127.0.0.1:5000"
SECRET_KEY_IN_SOURCE = "pytodo-pro-dev-secret"   # app.py line: app.config["SECRET_KEY"]

# ---- Web (HTML) routes ----
LOGIN_URL = "/login"           # form fields: username, password
LOGOUT_URL = "/logout"
HOME_URL = "/"
DASHBOARD_URL = "/dashboard"

# ---- JSON API routes ----
API_REGISTER = "/api/register"   # {"username","password"}
API_LOGIN = "/api/login"         # {"username","password"}
API_TASKS = "/api/tasks"         # GET ?category=&status=&q=&page=&per_page=   POST create
API_TASK = "/api/tasks/{id}"     # GET / PUT / DELETE
API_DASHBOARD = "/api/dashboard"
API_CATEGORIES = "/api/categories"
SEARCH_PARAM = "q"
PER_PAGE_PARAM = "per_page"

VALID_CATEGORY_ID = 1            # categories seeded: Work, Personal, Study, Urgent
VALID_DUE_DATE = "2026-12-31"

# ---- Test accounts (created automatically). Password must be 9+ chars (DEF-001). ----
PASSWORD = "Passw0rd!23"
USER_A = "sec_user_a"
USER_B = "sec_user_b"

# ---- Performance test ----
PERF_USER_PREFIX = "perf_user_"
PERF_USERS = 20
TASKS_PER_PERF_USER = 50
