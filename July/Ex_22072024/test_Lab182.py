import pytest


@pytest.mark.smoke
def test_sub():
    assert 4 - 1 == 3


@pytest.mark.regression
def test_sub1():
    assert 5 - 4 == 1


@pytest.mark.retest
def test_sum():
    assert 4 + 3 == 7

@pytest.mark.sanity
def test_sum2():
    assert 4 + 9 == 13

@pytest.mark.skip(reason= "Not working,so skip it")
def test_sum3():
    assert 9 + 9 == 18


