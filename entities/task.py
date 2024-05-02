from __future__ import annotations

import logging

from config.config import URL_TODO
from helpers.rest_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class Task:
    def __init__(self, rest_client=None, task_content=None, priority=3):
        self.url_todo_tasks = f"{URL_TODO}/tasks"
        self.rest_client = rest_client
        if rest_client is None:
            self.rest_client = RestClient()
        self.task_content = task_content
        self.priority = priority

    def create_task(self):
        if self.task_content is None:
            self.task_content = "Task content object"

        body_task = {
            "content": self.task_content,
            "due_string": "tomorrow at 12:00",
            "due_lang": "en",
            "priority": self.priority,
        }
        response = self.rest_client.request(
            "post",
            self.url_todo_tasks,
            body=body_task,
        )

        return response

    # def delete_task(self, project_id):
    #     LOGGER.debug("Cleanup project")
    #     url_delete_project = f"{URL_TODO}/projects/{project_id}"
    #     response = self.rest_client.request("delete", url_delete_project)
    #     if response["status_code"] == 204:
    #         LOGGER.info("project Id deleted : %s", project_id)


if __name__ == '__main__':
    t = Task(task_content="Task test ET")
    t.create_task()
