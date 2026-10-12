import requests 
from pytest_bdd import scenarios, then, parsers, when

scenarios("../features/users.feature")
#  ---- When ----

@when("I request the list of users", 
      target_fixture="response")
def request_users_list(base_url, auth_headers):
    return requests.get(f"{base_url}/users", headers=auth_headers, timeout=10)

@when(parsers.parse('I request the user with id {user_id:d}'), 
      target_fixture="response")
def request_user(base_url, auth_headers, user_id):
    return requests.get(f"{base_url}/users/{user_id}", headers=auth_headers, timeout=10)

#  ---- Then ----
@then("the list is not empty")
def list_not_empty(response):
    assert len(response.json()["data"]) > 0

@then("every user has an id")
def every_user_has_an_id(response):
    items = response.json()["data"]
    for item in items: 
        assert item['id'] is not None, f"Item {item} does not have an id"

