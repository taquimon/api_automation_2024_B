from dotenv import load_dotenv
import os

load_dotenv()

token_todo_api = os.getenv("token")

URL_TODO = "https://api.todoist.com/rest/v2"
HEADERS_TODO = {
    "Authorization": f"Bearer {token_todo_api}"
}
