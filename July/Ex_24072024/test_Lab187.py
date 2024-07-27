# FULL CRUD
import allure
import pytest
import requests


@allure.title("Create BooKING CRUD")
@allure.description("TC#1 - Verify that a booking is created")
@pytest.mark.crud
def test_create_booking_positive():
    # to make a  request
    # url
    # method - POST
    # header- Content-Type=application/json
    # payload
    # Auth - No
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
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


    response=requests.post(url=URL, headers=headers, json=payload)

    assert response.status_code == 200

    responseData= response.json()

    assert responseData["bookingid"] != None
    assert responseData["bookingid"] > 0
    assert type(responseData["bookingid"]) == int
    first_name= responseData["booking"]["firstname"]
    last_name= responseData["booking"]["lastname"]
    assert first_name == "Swapy"
    assert last_name == "Kakade"


@allure.title("Create BooKING CRUD")
@allure.description("TC#2 - Verify that a booking is created with payload {}")
@pytest.mark.crud
def test_create_booking_negative():
    # to make a  request
    # url
    # method - POST
    # header- Content-Type=application/json
    # payload
    # Auth - No
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-type": "application/json"}
    json_payload = {}

    response=requests.post(url=URL, headers=headers, json=json_payload)

    assert response.status_code == 500
    print(type(URL))
    print(type(headers))
    print(type(json_payload))



