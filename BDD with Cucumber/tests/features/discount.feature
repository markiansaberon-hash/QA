Feature: Discount rules

  Scenario Outline: Tiered discounts by spend
    Given an empty shopping cart
    When I add a "<product>" priced at <price>
    Then the discount applied should be <discount>

    Examples:
      | product  | price  | discount |
      | Keyboard | 49.99  | 0.0      |
      | Monitor  | 250.00 | 25.0     |
      | Laptop   | 1200.0 | 180.0    |