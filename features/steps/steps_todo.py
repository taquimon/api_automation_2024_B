"""
(c) Copyright Jalasoft. 2024

steps_todo.py
    file contains all steps definitions for feature files
"""
import json
import logging

from behave import when, then
from utils.logger import get_logger


LOGGER = get_logger(__name__, logging.DEBUG)


@when('I call to "{endpoint}" endpoint using "GET" option and with parameters')
def step_call_get_endpoint(context, endpoint):
    """
    step to call get endpoint
    :param context:
    :param endpoint:
    """
    LOGGER.debug("STEP: When I call to '%s' endpoint using 'GET' "
                 "option and with parameters", endpoint)
    url_endpoint = get_url_by_feature(context, endpoint)
    response = context.rest_client.request("get", url_endpoint)
    context.response = response
    context.endpoint = endpoint


@when('I call to "{endpoint}" endpoint using "POST" option and with parameters')
def step_call_post_endpoint(context, endpoint):
    """
    Step to call post endpoint
    :param context:
    :param endpoint:
    """
    LOGGER.debug('STEP: When I call to "%s" endpoint using "POST" '
                 'option and with parameters', endpoint)
    url_endpoint = get_url_by_feature(context, endpoint)
    body_endpoint = {}
    if context.text:
        LOGGER.debug("JSON Docstring: %s", context.text)
        body_endpoint = update_json_param(context, json.loads(context.text))
    else:
        body_endpoint = {
            "name": "Complete task C#",
            "color": "orange"
        }
    response = context.rest_client.request("post", url_endpoint, body=body_endpoint)
    # add to list of resources the resource created (id)
    resource_id = response["body"]["id"]
    context.resource_list[endpoint].append(resource_id)
    # store in context response and endpoint
    context.response = response
    context.endpoint = endpoint


@when('I call to "{endpoint}" endpoint using "DELETE" option and with parameters')
def step_call_delete_endpoint(context, endpoint):
    """
    Step to call delete endpoint
    :param context:
    :param endpoint:
    """
    LOGGER.debug('STEP: When I call to "%s" endpoint using "DELETE" '
                 'option and with parameters', endpoint)

    url_delete_project = get_url_by_feature(context, endpoint, resource_id=True)
    response = context.rest_client.request("delete", url_delete_project)
    context.response = response
    context.endpoint = endpoint


@then('I receive the response and validate with "{json_file}" file')
def step_receive_response(context, json_file):
    """
    Step to receive response
    :param context:
    :param json_file:
    """
    LOGGER.debug('STEP: Then I receive the response and validate')
    context.validate.validate_response(context.response, context.endpoint, json_file)


@then('I validate the status code is {status_code:d}')
def step_validate_status_code(context, status_code):
    """
    Step to validate the status code
    :param context:
    :param status_code:
    """
    LOGGER.debug("STEP: Then I validate the status code is %s", status_code)
    assert context.response["status_code"] == status_code, \
        f"Expected {status_code} but received {context.response['status_code']}"


def get_url_by_feature(context, endpoint, resource_id=False):
    """

    :param context:
    :param endpoint:
    :param resource_id:
    :return:
    """
    url = None
    if endpoint == "projects":
        if resource_id:
            if hasattr(context, "project_id"):
                url = context.url_todo_projects + "/" + context.project_id
        else:
            url = context.url_todo_projects
    elif endpoint == "sections":
        if resource_id:
            if hasattr(context, "section_id"):
                url = context.url_todo_sections + "/" + context.section_id
        else:
            url = context.url_todo_sections
    elif endpoint == "tasks":
        return context.url_todo_tasks

    return url


def update_json_param(context, json_data):
    """

    :param context:
    :param json_data:
    :return:
    """
    keys = ["project_id", "section_id", "task_id"]
    for k in keys:
        for d in json_data.keys():
            if d == k and hasattr(context, k):
                json_data[d] = getattr(context, k) # "project_id" = "2124123"
                LOGGER.debug("Key changed %s: ", d)
    LOGGER.debug("New JSON data: %s", json_data)

    return json_data
