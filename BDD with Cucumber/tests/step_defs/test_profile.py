import requests 
from pytest_bdd import scenarios, then, parsers, when

scenarios("../features/profile.feature")

# ---- When ----

@when(("I request my profile without a token"), 
      target_fixture="response")
def request_profile_without_headers(base_url):
    return requests.get(f"{base_url}/auth/me",
                        timeout=10)

@when(("I request my profile"),
      target_fixture="response")
def request_profile_with_headers(base_url, auth_headers):
    return requests.get(f"{base_url}/auth/me",
                        headers=auth_headers, timeout=10)

# ---- Then ----

@then(parsers.parse('the profile email is "{email}"'))
def check_email(response,email):
    assert response.json()["data"]["email"] == email