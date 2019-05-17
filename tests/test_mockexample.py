import pytest
from pytest_mock import mocker
from src.MockExample import Person
from src.MockExample import DB

@pytest.fixture
def test_save(mocker):
    return mocker.patch.object(DB,'persist')

def test_per(test_save):
    gabe=Person("Gabe",test_save)
    gabe.save()
    test_save.persist.assert_called_with(gabe)
