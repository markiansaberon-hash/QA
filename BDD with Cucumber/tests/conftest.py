import pytest
import requests
from pytest_bdd import when, then, given, parsers

@pytest.fixture(scope="session")
def base_url():
    return 'https://api.qaautomationlabs.com/v1'

# ---- Given ----
@given("I am logged in", target_fixture="auth_headers")
def logged_in(base_url):
    r = requests.post(f"{base_url}/auth/login",
                      json={"email": "qa@demo.io", "password": "Password123"}, timeout=10)
    assert r.status_code == 200
    token = r.json()["data"]["accessToken"]
    return {"Authorization": f"Bearer {token}"}

# ---- When ----
@when(parsers.parse('I log in with email "{email}" and password "{password}"'),
      target_fixture="response")
def login(base_url, email, password):
    return requests.post(f"{base_url}/auth/login",
                         json={"email": email, "password": password}, timeout=10)

# ---- Then ----
@then(parsers.parse("the response status is {status:d}"))
def check_status(response, status):
    assert response.status_code == status

@then(parsers.parse('the error code is "{code}"'))
def check_errorcode(response, code):
    assert response.json()["error"]["code"] == code