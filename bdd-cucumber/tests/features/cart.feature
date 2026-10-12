Feature: shopping cart totals
    As a shopper
    I want my cart to calculate totals correctly 
    So that I am charged the right amount 

    Scenario: Adding a single item 
        Given an empty shopping cart 
        When I add a "Keyboard" priced at 49.99
        Then the cart total should be 49.99
        And the cart should contain 1 item 

    Scenario: Adding two different items
        Given an empty shopping cart 
        When I add a "Keyboard" priced at 49.99
        When I add a "Mouse" priced at 19.99
        Then the cart total should be 69.98
        And the cart should contain 2 items

