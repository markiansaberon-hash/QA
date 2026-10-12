import requests 
from pytest_bdd import scenarios, when, then, parsers

scenarios("../features/login.feature")

@when(parsers.parse('I log in with email "{email}" and password "{password}"'), 
      target_fixture="response")
def login(base_url, email, password):
    return requests.post(f"{base_url}/auth/login", 
                         json={"email": email, "password": password}, timeout=10)

@then(parsers.parse("the response status is {status:d}"))
def check_status(response, status):
    assert response.status_code == status

@then("the response contains an access token")
def check_token(response):
    assert response.json()["data"]["accessToken"]