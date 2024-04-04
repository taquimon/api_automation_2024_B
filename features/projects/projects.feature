@projects
Feature: Projects

  # Title of test case
  @acceptance
  Scenario: Verify that get all projects endpoint return all the projects created
    As I user I want to get all projects in TODOIST API

    Given I set the URL and headers
    When I call to "projects" endpoint using "GET" option and with parameters
    Then I receive the response and validate
    And I validate the status code is 200

  @project_id  @acceptance
  Scenario: Verify that create project endpoint return a project created
    As I user I want to create a project in TODOIST API

    Given I set the URL and headers
    When I call to "sections" endpoint using "POST" option and with parameters
    Then I receive the response and validate
    And I validate the status code is 204