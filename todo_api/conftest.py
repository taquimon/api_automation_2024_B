import logging

import pytest
import requests

from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


@pytest.fixture()
def create_project():
    project_id = None
    LOGGER.info("Fixture create project")
    body_project = {
        "name": "Project from Fixture",
        "color": "orange"
    }
    token = "9463fd6e63c3ac3e06372045795ef48264968d2c"
    url_todo_projects = "https://api.todoist.com/rest/v2/projects"
    headers = {
            "Authorization": f"Bearer {token}"
    }
    response = requests.post(url_todo_projects, headers=headers, data=body_project)
    LOGGER.debug("Response to create project(json): %s", response.json())
    LOGGER.debug("Status Code: %s", response.status_code)
    if response.status_code == 200:
        project_id = response.json()["id"]

    return project_id
