
import pytest

from api import get_maltese

# def test_given_a_working_internet_connection_when_requesting_dogs_then_ok_is_returned():
#     dog = get_maltese()
#     assert(dog.status_code == 200)

def test_given_a_working_internet_connection_when_requesting_dogs_then_ok_is_returned():
    status_code, dog = get_maltese()
    expected_value = 200
    assert(status_code == expected_value)

def test_given_a_working_internet_connection_when_requesting_dogs_then_url_begins_with_maltese():
    status_code, dog = get_maltese()
    last_slash = dog.rfind('/')
    value = dog[:last_slash]
    expected_value = 'https://images.dog.ceo/breeds/maltese'
    assert(value == expected_value)