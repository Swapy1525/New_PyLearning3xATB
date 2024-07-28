import pytest


@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def booking_id():
    return '122213'

def test_update_request_1(create_token,booking_id):
    print("token=", create_token)
    print("booking_id=", booking_id)

def test_update_request_2(create_token,booking_id):
    print("token=", create_token)
    print("booking_id=", booking_id)



