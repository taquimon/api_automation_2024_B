import logging
import unittest

import allure
from nose2.tools import params

from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestNose2Example(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Setup class
        """
        LOGGER.warning("Setup class")

    def setUp(self):
        """
        Setup method
        """
        LOGGER.warning("Setup method")

    def tearDown(self):
        """
        teardown method
        """
        LOGGER.warning("teardown method")

    def test_one(self):
        """
        Test one
        """
        LOGGER.debug("Test One")

    def test_two(self):
        """
        Test one
        """
        LOGGER.debug("Test two")

    @allure.story("Test wit parameters")
    @params("one", "two", "three")
    def test_three(self, param):
        """
        Test one
        """
        LOGGER.debug("Test three param: %s", param)

    @classmethod
    def tearDownClass(cls):
        """
        teardown class
        """
        LOGGER.warning("Teardown class")
