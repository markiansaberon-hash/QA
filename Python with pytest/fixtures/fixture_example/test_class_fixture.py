import pytest

@pytest.fixture(scope="class")
def setup_class_data(request): 

    # Setup code
    print("\nSetting up class data...")
    request.cls.user_name = "test_user"
    request.cls.email = "test_user@example.com"

    yield  # This is where the test methods will run

    # Teardown code
    print("\nTearing down class data...")

@pytest.mark.usefixtures(setup_class_data)
class testUserActions: 
    def test_user_login(self): 
        print(f"Running test_user_login with user_name: {self.user_name} and email: {self.email}")
        assert self.user_name == "test_user"
        assert self.email == "test_user@example.com"