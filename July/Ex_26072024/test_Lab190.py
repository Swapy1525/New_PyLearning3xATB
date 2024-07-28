# Fixture - Concept in python
# You can use the fixture
# used to provide context to the test.
# Similar - pre condition, post condition.

# Pre Condition - token, booking Id - Fixture
# test_Update_negative 1
# test_Update_postitive 2


# setUp and TearDown- Pre and Post condition.
import pytest


@pytest.fixture()
def isMarried():
    return True

def test_i_need_confim(isMarried):
    assert isMarried == True

