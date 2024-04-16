@projects
Feature: Projects

  # Title of test case
  @critical
  @allure.label.owner:Edwin_Taquichiri
  @allure.link:https://dev.example.com/
  @allure.issue:API-123
  @acceptance
  Scenario: Verify that get all projects endpoint return all the projects created
    As I user I want to get all projects in TODOIST API

    When I call to "projects" endpoint using "GET" option and with parameters
    Then I receive the response and validate with "get_all_projects" file
    And I validate the status code is 200

  @normal
  @allure.label.owner:Edwin_Taquichiri
  @allure.link:https://dev.example.com/
  @allure.issue:API-123
  @acceptance
  Scenario: Verify that create project endpoint return a project created
    As I user I want to create a project in TODOIST API

    When I call to "projects" endpoint using "POST" option and with parameters
    Then I receive the response and validate with "create_project" file
    And I validate the status code is 200

  @trivial
  @allure.label.owner:Edwin_Taquichiri
  @allure.link:https://dev.example.com/
  @allure.issue:API-123
  @project_id  @acceptance
  Scenario: Verify that delete project endpoint deletes the project
    As I user I want to delete a project in TODOIST API

    When I call to "projects" endpoint using "DELETE" option and with parameters
    Then I receive the response and validate with "delete_project" file
    And I validate the status code is 204