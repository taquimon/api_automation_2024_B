from __future__ import annotations

import logging

from config.config import URL_TODO
from helpers.rest_client import RestClient
from helpers.validate_response import ValidateResponse
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
        self.validate = ValidateResponse()

    def create_task(self, file=False, number_tasks=0):
        if self.task_content is None:
            self.task_content = "Task content object"
        response_list = []
        body_task = {
            "content": self.task_content,
            "due_string": "tomorrow at 12:00",
            "due_lang": "en",
            "priority": self.priority,
        }
        if file:
            data_task = self.validate.read_input_data_json("/home/berserker/python/api_automation_2024_B/todo_api/input_data/tasks/tasks.json")

            for index in range(0, number_tasks):
                body_task = data_task[index]
                response = self.rest_client.request(
                    "post",
                    self.url_todo_tasks,
                    body=body_task,
                )
        else:
            response = self.rest_client.request(
                "post",
                self.url_todo_tasks,
                body=body_task,
            )
        response_list.append(response)
        return response_list

    # def delete_task(self, project_id):
    #     LOGGER.debug("Cleanup project")
    #     url_delete_project = f"{URL_TODO}/projects/{project_id}"
    #     response = self.rest_client.request("delete", url_delete_project)
    #     if response["status_code"] == 204:
    #         LOGGER.info("project Id deleted : %s", project_id)


if __name__ == '__main__':
    t = Task()
    t.create_task(file=True, number_tasks=4)
