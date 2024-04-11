@tasks
Feature: Tasks

  # Title of test case
  @acceptance
  Scenario: Verify that get all projects endpoint return all the projects created
    As I user I want to get all projects in TODOIST API

    When I call to "tasks" endpoint using "GET" option and with parameters
    Then I validate the status code is 200