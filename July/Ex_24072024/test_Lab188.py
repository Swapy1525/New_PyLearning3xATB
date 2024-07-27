# PUT request - update a booking
# url
# path - booking id
# path param
# token'


import requests


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

    # assertion
    assert response.status_code == 200
    # get response body and verify json
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id


def test_create_put_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    PUT_URL = base_url + base_path

    cookie = "token=" + create_token()
    headers = {
        "Content-type": "application/json",
        "Cookie": cookie

    }
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

    response = requests.put(url=PUT_URL, headers=headers, json=payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Swapy"

# to delete the newly created booking


def test_delete_booking():
    url = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    delete_url = url + str(booking_id)
    cookie = "token=" + create_token()
    headers = {
        "Content-type": "application/json",
        "Cookie": cookie
    }
    print(headers)

    response= requests.delete(url= delete_url, headers= headers)



