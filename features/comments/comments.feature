@comments
Feature: Comments

  # Title of test case
  @acceptance @stub @get_comment
  Scenario: Verify that get comment endpoint return a comment
    As I user I want to get a comment in TODOIST API

    When I call to "comment" endpoint using "GET" option and with parameters
    """
    {
      "stub": "True"
    }
    """
    Then I validate the status code is 200
