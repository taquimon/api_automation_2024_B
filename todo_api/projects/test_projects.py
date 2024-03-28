import logging

import pytest

from config.config import URL_TODO, MAX_PROJECTS
from helpers.rest_client import RestClient
from helpers.validate_response import ValidateResponse
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestProjects:
    @classmethod
    def setup_class(cls):
        """
        Setup class for projects
        """
        cls.rest_client = RestClient()
        cls.url_todo_projects = f"{URL_TODO}/projects"
        response = cls.rest_client.request("get", cls.url_todo_projects)
        cls.project_id = response["body"][0]["id"]
        LOGGER.debug("Project ID: %s", cls.project_id)
        cls.project_list = []
        cls.validate = ValidateResponse()

    def test_get_all_projects(self, log_test_names):
        """
        Test get all projects endpoint
        """
        LOGGER.info("Test get all projects")
        response = self.rest_client.request("get", self.url_todo_projects)

        self.validate.validate_response(response, "projects", "get_all_projects")

    def test_get_project(self, log_test_names):
        """
        Test get project endpoint
        """
        LOGGER.info("Test get project")
        url_get_project = f"{self.url_todo_projects}/{self.project_id}"
        response = self.rest_client.request("get", url_get_project)

        assert response["status_code"] == 200

    def test_create_project(self, log_test_names):
        """
        Test create project
        """
        LOGGER.info("Test create project")
        body_project = {
            "name": "Complete task C#",
            "color": "orange"
        }
        response = self.rest_client.request("post", self.url_todo_projects, body=body_project)
        if response["status_code"] == 200:
            self.project_list.append(response["body"]["id"])

        self.validate.validate_response(response, "projects", "create_project")

    def test_delete_project(self, create_project, log_test_names):
        """
        Test delete project
        """
        LOGGER.info("Test delete project")
        url_delete_project = f"{self.url_todo_projects}/{create_project}"
        LOGGER.info("project Id to be deleted : %s", create_project)
        response = self.rest_client.request("delete", url_delete_project)

        self.validate.validate_response(response, "projects", "delete_project")

    def test_update_project(self, create_project, log_test_names):
        """

        :param create_project:
        :param log_test_names:
        :return:
        """
        LOGGER.info("Test update project")
        url_delete_project = f"{self.url_todo_projects}/{create_project}"
        body_update_project = {
            "name": "Updated project",
            "color": "orange",
            "is_favorite": True
        }
        # call to endpoint:
        response = self.rest_client.request("post", url_delete_project, body=body_update_project)
        if response["status_code"] == 200:
            self.project_list.append(response["body"]["id"])

        self.validate.validate_response(response, "projects", "update_project")

    @pytest.mark.functional
    def test_max_number_projects(self,log_test_names):

        response = self.rest_client.request("get", self.url_todo_projects)
        number_of_projects = len(response["body"])
        LOGGER.debug("Number of current projects: %s", number_of_projects)
        for index in range(number_of_projects, MAX_PROJECTS):
            body_project = {
                "name": f"Project {index}",
                "color": "orange"
            }
            response = self.rest_client.request("post", self.url_todo_projects, body=body_project)
            self.project_list.append(response["body"]["id"])

        body_project = {
            "name": "Last Project",
            "color": "orange"
        }
        response = self.rest_client.request("post", self.url_todo_projects, body=body_project)

        self.validate.validate_response(response, "projects", "max_project")

    @classmethod
    def teardown_class(cls):
        """
        PyTest teardown class
        """
        LOGGER.debug("Teardown class")
        LOGGER.debug("Cleanup projects data")
        for project_id in cls.project_list:
            url_delete_project = f"{cls.url_todo_projects}/{project_id}"
            response = cls.rest_client.request("delete", url_delete_project)
            if response["status_code"] == 204:
                LOGGER.info("project Id deleted : %s", project_id)

