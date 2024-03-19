import logging


from config.config import URL_TODO
from helpers.rest_client import RestClient
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
        cls.project_id = response.json()[0]["id"]
        LOGGER.debug("Project ID: %s", cls.project_id)
        cls.project_list = []

    def test_get_all_projects(self):
        """
        Test get all projects endpoint
        """
        LOGGER.info("Test get all projects")
        response = self.rest_client.request("get", self.url_todo_projects)

        assert response.status_code == 200

    def test_get_project(self):
        """
        Test get project endpoint
        """
        LOGGER.info("Test get project")
        url_get_project = f"{self.url_todo_projects}/{self.project_id}"
        response = self.rest_client.request("get", url_get_project)

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
        response = self.rest_client.request("post", self.url_todo_projects, body=body_project)
        if response.status_code == 200:
            self.project_list.append(response.json()["id"])

        assert response.status_code == 200

    def test_delete_project(self, create_project):
        """
        Test delete project
        """
        LOGGER.info("Test delete project")
        url_delete_project = f"{self.url_todo_projects}/{create_project}"
        LOGGER.info("project Id to be deleted : %s", create_project)
        response = self.rest_client.request("delete", url_delete_project)

        assert response.status_code == 204

    def test_update_project(self, create_project):
        LOGGER.info("Test update project")
        url_delete_project = f"{self.url_todo_projects}/{create_project}"
        body_update_project = {
            "name": "Updated project",
            "color": "orange",
            "is_favorite": True
        }
        response = self.rest_client.request("post", url_delete_project, body=body_update_project)
        if response.status_code == 200:
            self.project_list.append(response.json()["id"])

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
            response = cls.rest_client.request("delete", url_delete_project)
            if response.status_code == 204:
                LOGGER.info("project Id deleted : %s", project_id)

