"""
(c) Copyright Jalasoft. 2024

test_comments.py
    test class to run tests related to comments endpoint
"""
import logging

import pytest

from config.config import URL_TODO
from entities.project import Project
from helpers.rest_client import RestClient
from helpers.validate_response import ValidateResponse
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestProjects:
    """
    Class for projects tests
    """
    @classmethod
    def setup_class(cls):
        """
        Setup class for projects
        """
        cls.rest_client = RestClient()
        cls.url_todo_comments = "http://localhost:8088/__admin/mappings" # f"{URL_TODO}/projects"

        cls.comments_list = []
        cls.validate = ValidateResponse()
        # cls.project = Comment()

    @pytest.mark.acceptance
    def test_get_comment(self, _log_test_names):
        """
        Test get all projects endpoint
        """
        LOGGER.info("Test get comment")
        url_comment = f"{self.url_todo_comments}/3089db90-523c-4f33-a98f-8945d4021b5a"
        response = self.rest_client.request("get", url_comment)
        LOGGER.debug("Response Comment: %s", response)

        # self.validate.validate_response(response, "projects", "get_all_projects")
