import allure
import pytest

allure.title("TC#1 Verify sub function")
allure.description("this is a smoke test to verify subtraction function")
@pytest.mark.smoke
def test_sub():
    assert 4 - 1 == 3

allure.title("TC#2 Verify the sub function")
allure.description("this is a regression test to verify subtraction")
@pytest.mark.regression
def test_sub1():
    assert 5 - 4 == 1

allure.title("TC#3 Verify the addition function")
allure.description("this is a resting test to verify addition")
@pytest.mark.retest
def test_sum():
    assert 4 + 3 == 7

allure.title("TC#4 Verify the addition function")
allure.description("this is a sanity test to verify addition")
@pytest.mark.sanity
def test_sum2():
    assert 4 + 9 == 13

@pytest.mark.skip(reason= "Not working,so skip it")
def test_sum3():
    assert 9 + 9 == 18


