Feature: Reading users
    
    Scenario: List users
        Given I am logged in
        When I request the list of users
        Then the response status is 200
        And the list is not empty
        And every user has an id

    Scenario: Unknown users
        Given I am logged in
        When I request the user with id 999999
        Then the response status is 404
        And the error code is "NOT_FOUND"