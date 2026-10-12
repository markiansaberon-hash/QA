import requests 
from pytest_bdd import scenarios, then

scenarios("../features/login.feature")

@then("the response contains an access token")
def check_token(response):
    assert response.json()["data"]["accessToken"]