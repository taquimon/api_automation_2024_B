import logging

import pytest
import requests

from config.config import URL_TODO
from helpers.rest_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


@pytest.fixture()
def create_project():
    project_id = None
    rest_client = RestClient()
    LOGGER.info("Fixture create project")
    body_project = {
        "name": "Project from Fixture",
        "color": "orange"
    }
    url_todo_projects = f"{URL_TODO}/projects"
    response = rest_client.request("post", url_todo_projects, body=body_project)
    if response["status_code"] == 200:
        project_id = response["body"]["id"]

    yield project_id
    LOGGER.debug("Yield fixture delete project")
    delete_project(project_id, rest_client)


@pytest.fixture()
def create_section(create_project):
    section_id = None
    LOGGER.info("Test create section")
    body_section = {
        "project_id": f"{create_project}",
        "name": "Section from fixture"
    }
    url_todo_sections = f"{URL_TODO}/sections"
    rest_client = RestClient()
    response = rest_client.request("post", url_todo_sections, body=body_section)
    if response.status_code == 200:
        section_id = response.json()["id"]
    return section_id


@pytest.fixture()
def create_task():
    task_id = None
    LOGGER.info("Fixture create task")
    body_task = {
            "content": "Task created from fixture",
            "due_string": "tomorrow at 12:00",
            "due_lang": "en",
            "priority": 4
    }
    url_todo_tasks = f"{URL_TODO}/tasks"
    rest_client = RestClient()
    response = rest_client.request("post", url_todo_tasks, body=body_task)
    if response["status_code"] == 200:
        task_id = response.json()["id"]
    yield task_id
    # delete task
    delete_task(task_id, rest_client)


def delete_project(project_id, rest_client):

    LOGGER.debug("Cleanup project")
    url_delete_project = f"{URL_TODO}/projects/{project_id}"
    response = rest_client.request("delete", url_delete_project)
    if response["status_code"] == 204:
        LOGGER.info("project Id deleted : %s", project_id)


def delete_task(task_id, rest_client):
    LOGGER.debug("Cleanup task")
    url_delete_task = f"{URL_TODO}/tasks/{task_id}"
    LOGGER.info("Task Id to be deleted : %s", task_id)
    response = rest_client.request("delete", url_delete_task)
    if response.status_code == 204:
        LOGGER.info("Task Id deleted : %s", task_id)


@pytest.fixture()
def log_test_names(request):
    LOGGER.info("Test '%s' STARTED", request.node.name)

    def fin():
        LOGGER.info("Test '%s' COMPLETED", request.node.name)

    request.addfinalizer(fin)