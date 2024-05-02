from __future__ import annotations

import logging

from helpers.rest_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestFastAPI:
    @classmethod
    def setup_class(cls):
        """
        Setup class for fast API
        """
        headers_fast_api = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        cls.rest_client = RestClient(headers=headers_fast_api)
        cls.url_fast_api = "http://127.0.0.1:8000/token"
        body_token = {
            "grant_type": "",
            "username": "etaquichiri",
            "password": "phantom",
            "scope": "",
            "client_id": "",
            "client_secret": "",
        }
        response = cls.rest_client.request("post", cls.url_fast_api, body=body_token)

        LOGGER.debug("Response token: %s", response["body"])
        cls.access_token = response["body"]["access_token"]

        headers_fast_api_endpoints = {
            "accept": "application/json",
            "Authorization": f"Bearer {cls.access_token}",
        }
        cls.rest_client_fast = RestClient(headers=headers_fast_api_endpoints)

    def test_get_users_me(self):
        """

        :return:
        """
        url_users = "http://127.0.0.1:8000/users/me/"

        response = self.rest_client_fast.request("get", url_users)

        LOGGER.debug("Response get current user: %s", response["body"])

        assert response["status_code"] == 200

    def test_get_users(self):
        """

        :return:
        """
        url_users = "http://127.0.0.1:8000/users"
        response = self.rest_client_fast.request("get", url_users)

        LOGGER.debug("Response get users: %s", response["body"])

        assert response["status_code"] == 200
