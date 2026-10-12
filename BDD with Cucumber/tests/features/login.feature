Feature: Login 

    Scenario: Valid credentials return an access token
        When I log in with email "qa@demo.io" and password "Password123"
        Then the response status is 200
        And the response contains an access token
    