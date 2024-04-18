"""
(c) Copyright Jalasoft 2024

environment.py
    file contains all environment functions/fixtures to be used by features
"""
import logging

from config.config import URL_TODO
from entities.project import Project
from helpers.rest_client import RestClient
from helpers.validate_response import ValidateResponse
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


def before_all(context):
    """
    Fixture to initialize variables and objects
    :param context:
    """
    LOGGER.info("Before all")
    context.rest_client = RestClient()
    context.url_todo_projects = f"{URL_TODO}/projects"
    context.url_todo_sections = f"{URL_TODO}/sections"
    context.url_todo_tasks = f"{URL_TODO}/tasks"
    # response = context.rest_client.request("get", context.url_todo_projects)
    # context.project_id = response["body"][0]["id"]
    # LOGGER.debug("Project ID: %s", context.project_id)
    context.resource_list = {
        "tasks": [],
        "sections": [],
        "projects": []
    }
    context.validate = ValidateResponse()
    context.project = Project()


# def before_feature(context, feature):
#     """
#
#     :param context:
#     :param feature:
#     """
#     LOGGER.info("Before feature")


def before_scenario(context, scenario):
    """

    :param context:
    :param scenario:
    """
    context.resource_list = {
        "tasks": [],
        "sections": [],
        "projects": []
    }
    LOGGER.info("Before Scenario")
    LOGGER.info("Test '%s' STARTED", scenario.name)

    if "project_id" in scenario.tags:
        new_project, _ = context.project.create_project()
        context.project_id = new_project["body"]["id"]
        context.resource_list["projects"].append(context.project_id)
        LOGGER.warning(context.resource_list)


def after_scenario(context, scenario):
    """

    :param context:
    :param scenario:
    """
    LOGGER.info("After scenario: %s", scenario.name)
    for resource in context.resource_list:
        for resource_id in context.resource_list[resource]:
            url_delete_project = f"{URL_TODO}/{resource}/{resource_id}"
            LOGGER.info("%s Id to be deleted : %s", resource, resource_id)
            response = context.rest_client.request("delete", url_delete_project)
            if response["status_code"] == 204:
                LOGGER.info("%s Id deleted : %s", resource, resource_id)


# def after_feature(context, feature):
#     """
#
#     :param context:
#     :param feature:
#     """
#     LOGGER.info("After feature")


# def after_all(context):
#     """
#
#     :param context:
#     """
#     LOGGER.info("After all")
