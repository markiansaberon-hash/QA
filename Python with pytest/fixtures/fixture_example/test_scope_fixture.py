import pytest 

@pytest.fixture(scope="session")
def session_scope_fixture():
    print("\nSetting up session scope fixture...")
    yield
    print("\nTearing down session scope fixture...")

@pytest.fixture(scope="function") #by default
def function_scope_fixture():
    print("\nSetting up function scope fixture...")
    yield
    print("\nTearing down function scope fixture...")

# @pytest.fixture(scope="module")
# def module_scope_fixture():
#     print("\nSetting up module scope fixture...")
#     yield
#     print("\nTearing down module scope fixture...")

# @pytest.fixture(scope="class")
# def class_scope_fixture():
#     print("\nSetting up class scope fixture...")
#     yield
#     print("\nTearing down class scope fixture...")

def test_one_using_scope(session_scope_fixture, function_scope_fixture):
    print ("\n>>>>Running test_one_using_scope...")
    assert True

def test_two_using_scope(session_scope_fixture, function_scope_fixture):
    print ("\n>>>>Running test_two_using_scope...")
    assert True
