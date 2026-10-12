Feature: Profile access

    Scenario: Profile requires a token 
        When I request my profile without a token
        Then the response status is 401
        And the error code is "UNAUTHORIZED"

    Scenario: Profile with a valid token 
        Given I am logged in
        When I request my profile
        Then the response status is 200
        And the profile email is "qa@demo.io"