from pytest_bdd import scenarios, given, when, then, parsers

# Load all scenarios from cart.feature as pytest tests
scenarios("../features/discount.feature")

@given("an empty shopping cart", target_fixture="cart")
def empty_cart():
    return Cart()

@when(parsers.parse("I add a {product:w} priced at {price:f}"))
def add_product(cart,product,price):
    assert cart.product == product
    assert cart.price == price 

@then(parsers.parse("the discount applied should be {discount:f}"))
def check_discount(cart, discount):
    assert cart.discount == discount
