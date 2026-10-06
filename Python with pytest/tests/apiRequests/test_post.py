import requests

def test_post_request_user(base_url, auth_headers):
    payload = {
        "firstName": "Ian",
        "lastName": "Testing",
        "email": "ada@qalabs.dev",
        "role": "engineer"
        }
    response = requests.post(f"{base_url}/users", json=payload, headers=auth_headers, timeout=10)
    assert response.status_code == 201
    print(response.json())

