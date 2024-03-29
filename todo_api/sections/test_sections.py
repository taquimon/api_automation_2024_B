import logging


from config.config import URL_TODO
from helpers.rest_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestSections:
    @classmethod
    def setup_class(cls):
        """
        Setup class for sections
        """
        cls.rest_client = RestClient()
        cls.url_todo_sections = f"{URL_TODO}/sections"

    def test_get_all_sections(self, log_test_names):
        """
        Test get all sections endpoint
        """
        response = self.rest_client.request("get", self.url_todo_sections)

        assert response.status_code == 200

    def test_get_all_sections_by_project(self, create_project, log_test_names):
        """
        Test get all section by project endpoint
        """
        LOGGER.info("Test get all sections by project")
        url_get_all_sections_by_project = f"{self.url_todo_sections}?project_id={create_project}"
        response = self.rest_client.request("get", url_get_all_sections_by_project)

        assert response.status_code == 200

    def test_get_section(self, create_section, log_test_names):
        """
        Test get section endpoint
        """
        LOGGER.info("Test get section")
        url_get_section = f"{self.url_todo_sections}/{create_section}"
        response = self.rest_client.request("get", url_get_section)

        assert response.status_code == 200

    def test_create_section(self, create_project, log_test_names):
        """
        Test create project
        """
        LOGGER.info("Test create section")
        body_section= {
            "project_id": f"{create_project}",
            "name": "Groceries"
        }
        response = self.rest_client.request("post", self.url_todo_sections, body=body_section)

        assert response.status_code == 200

    def test_delete_section(self, create_section, log_test_names):
        """
        Test delete project
        """
        LOGGER.info("Test delete section")
        url_delete_section = f"{self.url_todo_sections}/{create_section}"
        LOGGER.info("project Id to be deleted : %s", create_section)
        response = self.rest_client.request("delete", url_delete_section)

        assert response.status_code == 204

    def test_update_section(self, create_section, log_test_names):
        LOGGER.info("Test update section")
        url_update_section = f"{self.url_todo_sections}/{create_section}"
        body_update_section = {
            "name": "Updated section"
        }
        response = self.rest_client.request("post", url_update_section, body=body_update_section)

        assert response.status_code == 200

