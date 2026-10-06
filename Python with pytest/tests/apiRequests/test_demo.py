import pytest 
import requests

base_url = 'https://api.qaautomationlabs.com/v1'

@pytest.fixture()
def setup_api():
    # Setup code
    header = {
        'Content-Type': 'application/json'
    }
    print("Setting up the API test environment...")
    payload = {
        "email": "qa@demo.io",
            "password": "Password123"
        }
    response = requests.post(url=str(base_url + '/auth/login'), json=payload, headers=header)
    print(response.json())
    assert response.status_code == 200
    yield  response
    # Teardown code
    print("Tearing down the API test environment...")


def test_get_request(setup_api):
    token = setup_api.json()['data']['accessToken']
    header = {
        'Authorization': "Bearer " + token,
        'Content-Type': 'application/json'
    }
    response = requests.get(url= str (base_url+'/auth/me'), headers=header)
    print(response.json())
    assert response.status_code == 200