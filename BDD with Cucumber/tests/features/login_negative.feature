Feature: Invalid credentials are rejected

    Scenario Outline: Invalid credentials are rejected
            When I log in with email "<email>" and password "<password>"
            Then the response status is 401 
            And the error code is "INVALID_CREDENTIALS" 

        Examples: 
            | email          | password    |
            | qa@demo.io     | wrongpass   |
            | nobody@demo.io | Password123 | 