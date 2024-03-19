import logging


from config.config import URL_TODO
from helpers.rest_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestSections:
    @classmethod
    def setup_class(cls):
        """
        Setup class for projects
        """
        cls.rest_client = RestClient()
        cls.url_todo_sections = f"{URL_TODO}/sections"
        # response = cls.rest_client.request("get", cls.url_todo_sections)
        # cls.section_id = response.json()[0]["id"]
        # LOGGER.debug("Section ID: %s", cls.section_id)
        cls.section_list = []

    def test_get_all_sections(self):
        """
        Test get all sections endpoint
        """
        LOGGER.info("Test get all sections")
        response = self.rest_client.request("get", self.url_todo_sections)

        assert response.status_code == 200

    def test_get_all_sections_by_project(self, create_project):
        """
        Test get all section by project endpoint
        """
        LOGGER.info("Test get all sections")
        url_get_all_sections_by_project = f"{self.url_todo_sections}?project_id={create_project}"
        response = self.rest_client.request("get", url_get_all_sections_by_project)

        assert response.status_code == 200

    def test_get_section(self, create_section):
        """
        Test get project endpoint
        """
        LOGGER.info("Test get section")
        url_get_project = f"{self.url_todo_sections}/{create_section}"
        response = self.rest_client.request("get", url_get_project)

        assert response.status_code == 200

    def test_create_section(self, create_project):
        """
        Test create project
        """
        LOGGER.info("Test create section")
        body_section= {
            "project_id": f"{create_project}",
            "name": "Groceries"
        }
        response = self.rest_client.request("post", self.url_todo_sections, body=body_section)
        if response.status_code == 200:
            self.section_list.append(response.json()["id"])

        assert response.status_code == 200

    def test_delete_section(self, create_section):
        """
        Test delete project
        """
        LOGGER.info("Test delete section")
        url_delete_section = f"{self.url_todo_sections}/{create_section}"
        LOGGER.info("project Id to be deleted : %s", create_section)
        response = self.rest_client.request("delete", url_delete_section)

        assert response.status_code == 204

    def test_update_section(self, create_section):
        LOGGER.info("Test update section")
        url_update_section = f"{self.url_todo_sections}/{create_section}"
        body_update_section = {
            "name": "Updated section"
        }
        response = self.rest_client.request("post", url_update_section, body=body_update_section)
        if response.status_code == 200:
            self.section_list.append(response.json()["id"])

        assert response.status_code == 200
    #
    # @classmethod
    # def teardown_class(cls):
    #     """
    #     PyTest teardown class
    #     """
    #     LOGGER.debug("Teardown class")
    #     LOGGER.debug("Cleanup projects data")
    #     for project_id in cls.project_list:
    #         url_delete_project = f"{cls.url_todo_projects}/{project_id}"
    #         response = cls.rest_client.request("delete", url_delete_project)
    #         if response.status_code == 204:
    #             LOGGER.info("project Id deleted : %s", project_id)
    #
