"""
(c) Copyright Jalasoft. 2024

conftest_unittest.py
    configuration tes file to locate fixtures
"""
from __future__ import annotations

import logging

import pytest

from config.config import URL_TODO
from entities.project import Project
from helpers.rest_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


@pytest.fixture(name="create_project")
def create_project_fixture():
    """
    Fixture to create a project
    :return:
    """
    project_id = None

    LOGGER.info("Fixture create project")
    project = Project()
    response = project.create_project()
    if response["status_code"] == 200:
        project_id = response["body"]["id"]

    yield project_id
    LOGGER.debug("Yield fixture delete project")
    delete_project(project_id, project)


@pytest.fixture(name="create_section")
def create_section_fixture(create_project):
    """
    Fixture to create section
    :param create_project:
    """
    section_id = None
    LOGGER.info("Test create section")
    body_section = {
        "project_id": f"{create_project}",
        "name": "Section from fixture",
    }
    url_todo_sections = f"{URL_TODO}/sections"
    rest_client = RestClient()
    response = rest_client.request("post", url_todo_sections, body=body_section)
    if response["status_code"] == 200:
        section_id = response["body"]["id"]
    return section_id


@pytest.fixture(name="create_task")
def create_task_fixture():
    """
    Fixture to create a task
    """
    task_id = None
    LOGGER.info("Fixture create task")
    body_task = {
        "content": "Task created from fixture",
        "due_string": "tomorrow at 12:00",
        "due_lang": "en",
        "priority": 4,
    }
    url_todo_tasks = f"{URL_TODO}/tasks"
    rest_client = RestClient()
    response = rest_client.request("post", url_todo_tasks, body=body_task)
    if response["status_code"] == 200:
        task_id = response["body"]["id"]
    yield task_id
    # delete task
    delete_task(task_id, rest_client)


def delete_project(project_id, project):
    """
    Method to delete a project
    :param project_id:
    :param project:
    """
    project.delete_project(project_id)


def delete_task(task_id, rest_client):
    """
    Method to delete a task
    :param task_id:
    :param rest_client:
    """
    LOGGER.debug("Cleanup task")
    url_delete_task = f"{URL_TODO}/tasks/{task_id}"
    LOGGER.info("Task Id to be deleted : %s", task_id)
    response = rest_client.request("delete", url_delete_task)
    if response["status_code"] == 204:
        LOGGER.info("Task Id deleted : %s", task_id)


@pytest.fixture(name="_log_test_names")
def log_test_names_fixture(request):
    """
    Method to log start and end test
    :param request:
    """
    LOGGER.info("Test '%s' STARTED", request.node.name)

    def fin():
        LOGGER.info("Test '%s' COMPLETED", request.node.name)

    request.addfinalizer(fin)
