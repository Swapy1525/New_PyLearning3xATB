import allure
import pytest
import requests


@allure.title("Create BooKING CRUD")
@allure.description("TC#1 - Verify that a booking is created")
@pytest.mark.crud
def test_create_booking_positive():
    # Define the base URL and endpoint
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path

    # Define the headers and payload for the request
    headers = {"Content-type": "application/json"}
    payload = {
        "firstname": "Swapy",
        "lastname": "Kakade",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    # Make the POST request
    response = requests.post(url=URL, headers=headers, json=payload)

    # Assert the response status code
    assert response.status_code == 200

    # Parse the response JSON
    responseData = response.json()

    # Assert that bookingid is present and valid
    assert "bookingid" in responseData
    assert responseData["bookingid"] is not None
    assert responseData["bookingid"] > 0
    assert isinstance(responseData["bookingid"], int)

