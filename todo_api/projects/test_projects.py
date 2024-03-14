import logging

import requests

from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestProjects:
    @classmethod
    def setup_class(cls):
        """
        Setup class for projects
        """
        token = "9463fd6e63c3ac3e06372045795ef48264968d2c"
        cls.url_todo_projects = "https://api.todoist.com/rest/v2/projects"
        cls.headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(cls.url_todo_projects, headers=cls.headers)
        cls.project_id = response.json()[0]["id"]
        LOGGER.debug("Project ID: %s", cls.project_id)
        cls.project_list = []

    def test_get_all_projects(self):
        """
        Test get all projects endpoint
        """
        LOGGER.info("Test get all projects")
        response = requests.get(self.url_todo_projects, headers=self.headers)
        LOGGER.debug("Response to get all projects(text): %s", response.text)
        LOGGER.debug("Response to get all projects(json): %s", response.json())
        LOGGER.debug("Status Code: %s", response.status_code)
        assert response.status_code == 200

    def test_get_project(self):
        """
        Test get project endpoint
        """
        LOGGER.info("Test get project")
        url_get_project = f"{self.url_todo_projects}/{self.project_id}"
        response = requests.get(url_get_project, headers=self.headers)
        LOGGER.debug("Response to get project(json): %s", response.json())
        LOGGER.debug("Status Code: %s", response.status_code)
        assert response.status_code == 200

    def test_create_project(self):
        """
        Test create project
        """
        LOGGER.info("Test create project")
        body_project = {
            "name": "Complete task C#",
            "color": "orange"
        }
        response = requests.post(self.url_todo_projects, headers=self.headers, data=body_project)
        if response.status_code == 200:
            self.project_list.append(response.json()["id"])
        LOGGER.debug("Response to create project(json): %s", response.json())
        LOGGER.debug("Status Code: %s", response.status_code)
        assert response.status_code == 200

    def test_delete_project(self, create_project):
        """
        Test delete project
        """
        LOGGER.info("Test delete project")
        url_delete_project = f"{self.url_todo_projects}/{create_project}"
        LOGGER.info("project Id to be deleted : %s", create_project)
        response = requests.delete(url_delete_project, headers=self.headers)
        LOGGER.debug("Response to delete project(text): %s", response.text)
        LOGGER.debug("Status Code: %s", response.status_code)
        assert response.status_code == 204

    def test_update_project(self, create_project):
        LOGGER.info("Test update project")
        url_delete_project = f"{self.url_todo_projects}/{create_project}"
        body_update_project = {
            "name": "Updated project",
            "color": "orange",
            "is_favorite": True
        }
        response = requests.post(url_delete_project, headers=self.headers, data=body_update_project)
        if response.status_code == 200:
            self.project_list.append(response.json()["id"])
        LOGGER.debug("Response to delete project(json): %s", response.json())
        LOGGER.debug("Status Code: %s", response.status_code)
        assert response.status_code == 200

    @classmethod
    def teardown_class(cls):
        """
        PyTest teardown class
        """
        LOGGER.debug("Teardown class")
        LOGGER.debug("Cleanup projects data")
        for project_id in cls.project_list:
            url_delete_project = f"{cls.url_todo_projects}/{project_id}"
            response = requests.delete(url_delete_project, headers=cls.headers)
            if response.status_code == 204:
                LOGGER.info("project Id deleted : %s", project_id)

