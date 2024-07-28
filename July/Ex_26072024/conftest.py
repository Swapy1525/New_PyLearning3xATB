import pytest
import requests


@pytest.fixture()
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    header = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(url=url, headers=header, json=payload)
    token = response.json()["token"]
    print(token)
    return token


@pytest.fixture()
def create_booking():
    print("Create Booking Testcase")
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-type": "application/json"}
    payload = {
        "firstname": "john",
        "lastname": "Cena",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"

    }

    response = requests.post(url=url, headers=headers, json=payload)
    print(type(url))
    print(type(headers))
    print(type(payload))

    data = response.json()
    booking_id = data["bookingid"]
    return booking_id

@pytest.fixture
def read_csv_file_data():
    pass


@pytest.fixture
def read_mysql_file_database():
    pass


@pytest.fixture
def launch_browser():
    print("Launching a Browser!! Chrome")
    return "chrome"


@pytest.fixture
def close_browser():
    print("Closing a Browser!! Chrome")
    return "closed"


@pytest.fixture
def read_url_testdata_excel():
    pass