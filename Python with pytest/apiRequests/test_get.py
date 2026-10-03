import requests 

def test_get_request(base_url, auth_headers):
    response = requests.get(f"{base_url}/auth/me", headers=auth_headers, timeout=10)
    assert response.status_code == 200

def test_get_one_user(base_url, auth_headers): 
    id = 1
    response = requests.get(f"{base_url}/users/{id}", headers=auth_headers, timeout=10)
    assert response.status_code == 200
    print(response.json())


