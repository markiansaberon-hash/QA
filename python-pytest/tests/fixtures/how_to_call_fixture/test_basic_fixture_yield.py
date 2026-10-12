import pytest 

@pytest.fixture
def setup_and_teardown(): 
    # Setup code
    print("Setting up the test environment...")
    yield  # This is where the test function will run
    # Teardown code
    print("Tearing down the test environment...")


@pytest.mark.usefixtures("setup_and_teardown")
def test_example_using_usefixtures_decorator(): 
    print("Running the test function... not the setup_and_teardown fixture...")
    # assert True

