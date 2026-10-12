from pytest_bdd import scenarios, given, when, then, parsers
from shopping.cart import Cart
# Load all scenarios from cart.feature as pytest tests
scenarios("../features/cart.feature")

# @pytest.mark.smoke
# @scenario("../features/cart.feature", "Adding a single item")
# def test_single_item():
#     # The decorated function body runs AFTER all steps complete.
#     pass

@given("an empty shopping cart", target_fixture="cart")
def empty_cart():
    return Cart()

@when(parsers.parse('I add a "{name}" priced at {price:f}'))
def add_item(cart,name,price):
    cart.add(name,price)

@then(parsers.parse("the cart total should be {expected:f}"))
def check_total(cart,expected):
    assert cart.total == expected

@then(parsers.parse("the cart should contain {count:d} item"))
@then(parsers.parse("the cart should contain {count:d} items"))
def check_count(cart, count):
    assert len(cart.items) == count 



