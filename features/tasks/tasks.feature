@tasks
Feature: Tasks

  # Title of test case
  @acceptance
  Scenario: Verify that get all projects endpoint return all the projects created
    As I user I want to get all projects in TODOIST API

    When I call to "tasks" endpoint using "GET" option and with parameters
    Then I validate the status code is 200

  Scenario:   Verify I can create a task in TODOIST API
    When I create a task "Task created using data type" in TODOIST API
    Then I validate the status code is 200

  Scenario: Verify I can create multiple tasks
    When I create a task "<task_content><priority>" in TODOIST API
    | task_content_title |  priority |
    | Task 1: Make the homework            | 2 |
    | Task 2: Make the dinner              | 1 |
    | Task 3: Pay money to bank            | 3 |
