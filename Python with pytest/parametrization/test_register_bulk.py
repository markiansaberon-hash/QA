import requests 
import pytest

@pytest.mark.parametrize("payload, expected_status", [
    ({"firstname": "fname1", "lastname": "lname1", "email": "fname1.lname1@example.com", "role": "engineer"}, 201), 
    ({"firstname": "fname2", "lastname": "lname2", "email": "fname2.lname2@example.com", "role": "manager"}, 201),
    ({"firstname": "fname3", "lastname": "lname3", "email": "fname3.lname3@example.com", "role": "developer"}, 201),
    ({"firstname": "fname4", "lastname": "lname4", "email": "fname4.lname4@example.com", "role": "designer"}, 201),
    ({"firstname": "fname5", "lastname": "lname5", "email": "fname5.lname5@example.com", "role": "tester"}, 201),
    ({"firstname": "fname2", "lastname": "lname2", "email": "fname2.lname2@example.com", "role": "manager"}, 201),
])
def test_register_bulk_users(base_url, auth_headers, payload, expected_status):
    payload = {"items": payload}
    print(f"Payload: {payload}")
    response = requests.post(f"{base_url}/users/bulk", json=payload, headers=auth_headers, timeout=10)
    assert response.status_code == expected_status
    items = response.json()['data']

    print("Each item gets an id")
    for item in items:
        assert item['id'] is not None, f"Item {item} does not have an id"

    print("The number of items in the response matches the number of items in the request")
    count = len(items)
    assert count == len(payload["items"])

    print("The response time is less than 1000 milliseconds")
    assert response.json()['meta']['responseTimeMs'] < 1000
