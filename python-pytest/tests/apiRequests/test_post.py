import requests
from jsonschema import validate

USER_SCHEMA = {
    "type": "object",
    "required": ["data"],
    "properties": {
        "data": {
            "type": "object",
            "required": ["id", "firstName", "lastName", "email", "role"],
            "properties": {
                "id": {"type": ["string", "integer"]},
                "firstName": {"type": "string"},
                "lastName": {"type": "string"},
                "email": {"type": "string", "format": "email"},
                "role": {"type": "string"},
            },
        }
    },
}

def test_post_request_user(base_url, auth_headers):
    payload = {
        "firstName": "Ian",
        "lastName": "Testing",
        "email": "ada@qalabs.dev",
        "role": "engineer"
        }
    response = requests.post(f"{base_url}/users", json=payload, headers=auth_headers, timeout=10)
    assert response.status_code == 201
    body = response.json()

    # Validate response structure against the schema
    validate(instance=body, schema=USER_SCHEMA)

    # Validate the values match what we sent
    assert body["data"]["email"] == payload["email"]
    assert body["data"]["role"] == payload["role"]



