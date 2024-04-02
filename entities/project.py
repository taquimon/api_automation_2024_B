import logging

from config.config import URL_TODO
from helpers.rest_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class Project:

    def __init__(self, rest_client=None):
        self.url_todo_projects = f"{URL_TODO}/projects"
        self.rest_client = rest_client
        if rest_client is None:
            self.rest_client = RestClient()

    def create_project(self, body=None):
        body_project = body
        if body is None:
            body_project = {
                "name": "Project from entity",
                "color": "orange"
            }
        response = self.rest_client.request("post", self.url_todo_projects, body=body_project)

        return response, self.rest_client

    def delete_project(self, project_id):
        LOGGER.debug("Cleanup project")
        url_delete_project = f"{URL_TODO}/projects/{project_id}"
        response = self.rest_client.request("delete", url_delete_project)
        if response["status_code"] == 204:
            LOGGER.info("project Id deleted : %s", project_id)
