Feature: Creating users

    Scenario: Create a user
        Given I am logged in
        When I create a user named "Ana" "Reyes" with email "ana.reyes@example.com" and role "engineer"
        Then the response status is 201
        And the created user has email "ana.reyes@example.com"
        And the created user has an id

    Scenario: Email is required
        Given I am logged in
        When I create a user without an email
        Then the response status is 422
        And the error code is "VALIDATION_ERROR"
        And the validation error is for the field "email"