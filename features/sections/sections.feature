@sections
Feature: Sections

  # Title of test case
  @acceptance
  Scenario: Verify that get all projects endpoint return all the projects created
    As I user I want to get all projects in TODOIST API

    When I call to "sections" endpoint using "GET" option and with parameters
    Then I validate the status code is 200


  @project_id @wip
  Scenario Outline: Verify that can be created several sections
      AS I user I want to create several sections in TODOIST API

      When I call to "sections" endpoint using "POST" option and with parameters
      """
      {
          "project_id": "project_id",
          "name": "<section_name>"
      }
      """

    Examples:
      | section_name   |
      | First Section  |
      | Second Section |
      | Third Section  |
      | Fourth Section |
