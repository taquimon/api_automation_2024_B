import logging

from utils.logger import get_logger
from behave import given, when, then, step

LOGGER = get_logger(__name__, logging.DEBUG)


@given(u'I set the URL and headers')
def step_impl(context):
    LOGGER.debug(u'STEP: Given I set the URL and headers')


@when(u'I call to "{endpoint}" endpoint using "{method_name}" option and with parameters')
def step_impl(context, endpoint, method_name):
    LOGGER.debug(f"STEP: When I call to '{endpoint}' endpoint using '{method_name}' option and with parameters")


@then(u'I receive the response and validate')
def step_impl(context):
    LOGGER.debug(u'STEP: Then I receive the response and validate')


@then(u'I validate the status code is {status_code:d}')
def step_impl(context, status_code):
    LOGGER.debug(f"STEP: Then I validate the status code is {status_code}")
