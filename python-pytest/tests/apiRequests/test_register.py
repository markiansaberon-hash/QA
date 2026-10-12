import requests 

def test_register_user(base_url, auth_headers):
    payload = {
        "name": "New User",
        "email": "new.user@example.com",
        "password": "Password123"
        }
    response = requests.post(f"{base_url}/auth/register", json=payload, headers=auth_headers, timeout=10)
    assert response.status_code == 201  
    data = response.json()['data']
    for key in ("id", "role", "accessToken"):
        assert data[key] is not None
    for key in ("name", "email"):
        assert data[key] == payload[key]

def test_register_user_with_incorrect_email(base_url, auth_headers):
    payload = {
        "name": "New User",
        "email": "new.user",
        "password": "Password123"
        }
    response = requests.post(f"{base_url}/auth/register", json=payload, headers=auth_headers, timeout=10)
    assert response.status_code == 422

