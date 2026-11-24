"""Create a fresh account seeded with Fixture Set A, for manual review sessions.

Usage (from the repository root, with `python app.py` running):

    python test/03_Special_Testing/seed_fixtures.py --initial e

Prints the username and password to log in with. Uses only the standard
library and the same data as the automated suites (fixtures.json).
"""

import argparse
import http.cookiejar
import json
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

DATA = json.loads((Path(__file__).resolve().parent / "fixtures.json").read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--initial", default=DATA["tester_initial"], help="reviewer initial for the username")
    parser.add_argument("--purpose", default="usa", help="username purpose segment (default: usa)")
    args = parser.parse_args()

    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

    def call(method, path, payload=None):
        body = None if payload is None else json.dumps(payload).encode()
        req = urllib.request.Request(DATA["base_url"] + path, data=body, method=method,
                                     headers={"Content-Type": "application/json"})
        with opener.open(req) as resp:
            return json.loads(resp.read() or b"null")

    username = f"w3{args.initial}_{args.purpose}_{datetime.now():%m%d%H%M%S}"
    assert len(username) <= 20, f"username too long: {username}"
    call("POST", "/api/register", {"username": username, "password": DATA["password"]})
    categories = {c["name"]: c["id"] for c in call("GET", "/api/categories")}
    for item in DATA["fixture_set_A"]:
        due = None if item["due_offset_days"] is None else (date.today() + timedelta(days=item["due_offset_days"])).isoformat()
        task = call("POST", "/api/tasks", {"title": item["title"], "description": item["description"],
                                           "category_id": categories.get(item["category"]), "due_date": due})
        if item["done"]:
            call("PUT", f"/api/tasks/{task['id']}", {"done": True})
    print(f"Seeded {len(DATA['fixture_set_A'])} tasks (Fixture Set A).")
    print(f"Log in at {DATA['base_url']}/login with username {username} and password {DATA['password']}")


if __name__ == "__main__":
    main()
