
import pytest

from api import get_maltese

# def test_given_a_working_internet_connection_when_requesting_dogs_then_ok_is_returned():
#     dog = get_maltese()
#     assert(dog.status_code == 200)

def test_given_a_working_internet_connection_when_requesting_dogs_then_ok_is_returned():
    status_code, dog = get_maltese()
    assert(status_code == 200)

