from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()

token_todo_api = os.getenv("token")
WEB_HOOK = os.getenv("WEB_HOOK")

URL_TODO = "https://api.todoist.com/rest/v2"
HEADERS_TODO = {
    "Authorization": f"Bearer {token_todo_api}",
}
abs_path = os.path.abspath(__file__ + "../../../")
MAX_PROJECTS = 8
