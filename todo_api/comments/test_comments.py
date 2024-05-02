"""
(c) Copyright Jalasoft. 2024

test_comments.py
    test class to run tests related to comments endpoint
"""
from __future__ import annotations

import logging

import pytest

from helpers.rest_client import RestClient
from helpers.validate_response import ValidateResponse
from utils.logger import get_logger
from utils.wiremock_stub import WiremockStub

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
        cls.url_todo_comments = (
            "http://localhost:8088/__admin/mappings"  # f"{URL_TODO}/projects"
        )

        cls.comments_list = []
        cls.validate = ValidateResponse()
        cls.wiremock_stub = WiremockStub()
        # cls.project = Comment()

    @pytest.mark.acceptance
    def test_get_comment(self, _log_test_names):
        """
        Test get all projects endpoint
        """
        LOGGER.info("Test get comment")
        # create stub
        response_stub, wiremock = self.wiremock_stub.create_stub(
            "comments",
            "get_comment",
        )
        comment_id_stub = response_stub["body"]["id"]
        LOGGER.debug("Get Comment Stub Id: %s", comment_id_stub)
        # test over stub created
        url_comment = (
            f"http://localhost:{wiremock.port}/__admin/mappings/{comment_id_stub}"
        )

        response = self.rest_client.request("get", url_comment)
        LOGGER.debug("Response Get Comment: %s", response)

        self.validate.validate_response(response, "comments", "get_comment", stub=True)

    @pytest.mark.acceptance
    def test_create_comment(self, _log_test_names):
        """
        Test get all projects endpoint
        """
        LOGGER.info("Test create comment")
        # create stub
        response_stub, wiremock = self.wiremock_stub.create_stub(
            "comments",
            "create_comment",
        )
        # test over stub created
        comment_id_stub = response_stub["body"]["id"]
        LOGGER.debug("Get Comment Stub Id: %s", comment_id_stub)
        # test over stub created
        url_comment = (
            f"http://localhost:{wiremock.port}/__admin/mappings/{comment_id_stub}"
        )

        response = self.rest_client.request("get", url_comment)
        LOGGER.debug("Response Create Comment: %s", response)
        self.validate.validate_response(
            response,
            "comments",
            "create_comment",
            stub=True,
        )
