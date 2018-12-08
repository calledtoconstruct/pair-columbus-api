
import pytest

from api import get_random_maltese

# def test_given_a_working_internet_connection_when_requesting_dogs_then_ok_is_returned():
#     dog = get_maltese()
#     assert(dog.status_code == 200)

def test_given_a_working_internet_connection_when_requesting_dogs_then_ok_is_returned():
    status_code, dog = get_random_maltese()
    expected_value = 200
    assert(status_code == expected_value)

def test_given_a_working_internet_connection_when_requesting_dogs_then_url_begins_with_maltese():
    status_code, dog = get_random_maltese()
    last_slash = dog.rfind('/')
    value = dog[:last_slash]
    expected_value = 'https://images.dog.ceo/breeds/maltese'
    assert(value == expected_value)

def test_given_a_working_internet_connect_when_requesting_dogs_twice_then_results_differ():

    status_code1, dog1 = get_random_maltese()
    last_slash1 = dog1.rfind('/')
    value1 = dog1[last_slash1:]

    status_code2, dog2 = get_random_maltese()
    last_slash2 = dog2.rfind('/')
    value2 = dog2[last_slash2:]

    assert(value1 != value2)
