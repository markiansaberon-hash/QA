import pytest
import requests

# @pytest.fixture(autouse=True)
# def disable_network_calls(monkeypatch):
#     def stunted_get():
#         raise RuntimeError("Network calls are disabled during tests.")
#     monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())

# @pytest.fixture
# def input_total():
#     total = 100
#     return total

@pytest.fixture(scope="session")
def base_url():
    return 'https://api.qaautomationlabs.com/v1'
    

@pytest.fixture(scope="session")
def auth_headers(base_url): 
    payload = {
        "email": "qa@demo.io",
        "password": "Password123"
    } 
    response = requests.post(f"{base_url}/auth/login", json=payload, timeout=10)
    assert response.status_code == 200
    token = response.json()['data']['accessToken']
    headers =  {"Authorization": f"Bearer {token}"}

    yield headers 

    requests.post(f"{base_url}/auth/logout", headers=headers, timeout=10)
    print("Logged out successfully.")