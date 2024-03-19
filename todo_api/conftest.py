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
    if response.status_code == 200:
        project_id = response.json()["id"]

    return project_id


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
