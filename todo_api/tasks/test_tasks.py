"""
(c) Copyright Jalasoft. 2024

test_task.py
    test class to run tests related to task endpoint
"""
import logging


from config.config import URL_TODO
from helpers.rest_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestTasks:
    """
    Class for tasks tests
    """
    @classmethod
    def setup_class(cls):
        """
        Setup class for tasks
        """
        cls.rest_client = RestClient()
        cls.url_todo_tasks = f"{URL_TODO}/tasks"

    def test_get_all_tasks(self, _log_test_names):
        """
        Test get all tasks endpoint
        """
        response = self.rest_client.request("get", self.url_todo_tasks)

        assert response["status_code"] == 200

    def test_get_task(self, create_task, _log_test_names):
        """
        Test get project endpoint
        """
        LOGGER.info("Test get section")
        url_get_task = f"{self.url_todo_tasks}/{create_task}"
        response = self.rest_client.request("get", url_get_task)

        assert response["status_code"] == 200

    def test_create_task(self, _log_test_names):
        """
        Test create task
        """
        LOGGER.info("Test create task")
        body_task= {
            "content": "Buy Milk",
            "due_string": "tomorrow at 12:00",
            "due_lang": "en",
            "priority": 4
        }
        response = self.rest_client.request("post", self.url_todo_tasks, body=body_task)

        assert response["status_code"] == 200

    def test_delete_task(self, create_task, _log_test_names):
        """
        Test delete task
        """
        LOGGER.info("Test delete task")
        url_delete_task = f"{self.url_todo_tasks}/{create_task}"
        LOGGER.info("project Id to be deleted : %s", create_task)
        response = self.rest_client.request("delete", url_delete_task)

        assert response["status_code"] == 204
