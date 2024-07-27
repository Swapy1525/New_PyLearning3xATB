# Request Module - A package / library containing functions
# which we can use easily (borrowing functionality from others)
# eg. math, os, allure, pytest
import allure
import pytest
import requests


# TO make the HTTP requests
# Request - MODULE
# GET, POST. PATCH , PUT, DELETE
# Supports url's, cookies, verification with pytest

# GET Request- booking id

# Request (client -> Server)

#url needed
# Auth !
# payload !
# content type !
# query param !
# path param needed

# Response
# we can verify
# body
# key and values
# status code
# Time
# JSON schema, XML Schema


@allure.title("test GET Request -Restful BOOKER project")
@allure.description("TC#1 - Verify that GET requestwith ID works")
@allure.tag("Regresion", "P0", "Smoke")
@allure.label("owner", "Swapy")
@allure.testcase("TC01")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response = requests.get(url)
    print(response.json())
    assert response.status_code ==200

@allure.title("test GET Request -Restful BOOKER project")
@allure.description("TC#2 - Verify that GET request with ID negative")
def test_get_single_request_by_id_neagative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    response1 = requests.get(url)
    assert response1.status_code==404

@allure.title("test GET Request -Restful BOOKER project")
@allure.description("TC#3 - Verify that GET request with ID negative")
def test_get_single_request_by_id_negative_1():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    response1 = requests.get(url)
    assert response1.status_code==200










