import requests 
from pytest_bdd import scenarios, when, then, parsers

scenarios("../features/login_negative.feature")

# @then(parsers.parse('the error code is "{code}"'))
# def check_errorcode(response, code):
#     assert response.json()["error"]["code"] == code
    
# Moved to conftest.py