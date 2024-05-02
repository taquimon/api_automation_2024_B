from behave import register_type
import parse

from entities.project import Project
from entities.task import Task


# class Task(object)
#     """
#     """


@parse.with_pattern(r"[^\"].+")
def parse_task(text):
    return Task(task_content=text)


@parse.with_pattern(r"[^\"].+")
def parse_project(text):
    return Project(project_name=text)


register_type(Task=parse_task)
register_type(Project=parse_project)
