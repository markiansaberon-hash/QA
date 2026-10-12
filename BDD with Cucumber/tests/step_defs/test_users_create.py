import requests 
from pytest_bdd import scenarios, then, parsers, when

scenarios("../features/users_create.feature")

#  ---- When ----
@when(parsers.parse('I create a user named "{fname}" "{lname}" with email "{email}" and role "{role}"'), 
      target_fixture="response")
def create_user(base_url, auth_headers, fname, lname, email, role):
    payload = {
        "firstName": fname, 
        "lastName": lname, 
        "email": email, 
        "role": role
        }
    return requests.post(f"{base_url}/users" ,json=payload, headers=auth_headers, timeout=10)

@when("I create a user without an email", 
      target_fixture="response")
def create_user_without_email(base_url, auth_headers):
    payload = {
        "firstName": "Boss", 
        "lastName": "Sab", 
        "role": "engineer"
        }
    return requests.post(f"{base_url}/users" , json=payload, headers=auth_headers, timeout=10)

#  ---- Then ----
@then(parsers.parse('the created user has email "{email}"'))
def verify_response_has_email(response, email):
    assert response.json()["data"]["email"] == email

@then("the created user has an id")
def verify_user_has_id(response):
    assert response.json()["data"]["id"] is not None

@then(parsers.parse('the validation error is for the field "{field}"'))
def verify_response_error_is_for_email(response, field):
    fields = [item["field"] for item in response.json()["error"]["details"]]
    assert field in fields, f"expected {field} in {fields}"