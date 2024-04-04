import logging

from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


def before_all(context):
    """

    :param context:
    """
    LOGGER.info("Before all")


def before_feature(context, feature):
    """

    :param context:
    :param feature:
    """
    LOGGER.info("Before feature")


def before_scenario(context, scenario):
    """

    :param context:
    :param scenario:
    """
    LOGGER.info("Before Scenario")


def after_scenario(context, scenario):
    """

    :param context:
    :param scenario:
    """
    LOGGER.info("After scenario")


def after_feature(context, feature):
    """

    :param context:
    :param feature:
    """
    LOGGER.info("After feature")


def after_all(context):
    """

    :param context:
    """
    LOGGER.info("After all")

