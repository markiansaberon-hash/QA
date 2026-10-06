import pytest
from format_data import format_data_for_display, format_data_for_excel

@pytest.fixture
def example_people_data():
    return [
        { 
            "first_name": "John", 
            "last_name": "Doe", 
            "title": "Software Engineer",
            "age": 30,
        }, 
        { 
            "first_name": "Jane", 
            "last_name": "Smith", 
            "title": "Data Scientist",
            "age": 28,
        },
        { 
            "first_name": "Alice", 
            "last_name": "Johnson", 
            "title": "Product Manager",
            "age": 35,
        },
    ]

# def test_format_data_for_display(): <--- use fixtures instead of hardcoding the data in the test function
#     people = [
#         { 
#             "first_name": "John", 
#             "last_name": "Doe", 
#             "title": "Software Engineer",
#             "age": 30,
#         }, 
#         { 
#             "first_name": "Jane", 
#             "last_name": "Smith", 
#             "title": "Data Scientist",
#             "age": 28,
#         },
#         { 
#             "first_name": "Alice", 
#             "last_name": "Johnson", 
#             "title": "Product Manager",
#             "age": 35,
#         },
#     ]

@pytest.mark.format
def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "John Doe, Software Engineer, 30 years old", 
        "Jane Smith, Data Scientist, 28 years old", 
        "Alice Johnson, Product Manager, 35 years old"]

@pytest.mark.format
def test_format_data_for_excel(example_people_data):
    assert format_data_for_excel(example_people_data) == """first_name,last_name,title,age
John,Doe,Software Engineer,30
Jane,Smith,Data Scientist,28
Alice,Johnson,Product Manager,35"""
