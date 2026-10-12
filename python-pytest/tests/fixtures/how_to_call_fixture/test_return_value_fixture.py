import pytest

@pytest.fixture
def user_credentials(): 

    print("\nSetting up user credentials...")
    credentials = {
        "username": "test_user",
        "password": "secure_password"
    }
    yield credentials  # This is where the test function will run

    print("Tearing down user credentials...")


def test_login_with_user_credentials(user_credentials):
    print("Running the test function...")
    print(user_credentials)
    print(f"this is the username: {user_credentials['username']}, this is the password: {user_credentials['password']}")
    assert user_credentials["username"] == "test_user"
    assert len(user_credentials["password"]) > 2

