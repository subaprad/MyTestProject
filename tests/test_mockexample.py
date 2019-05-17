import  pytest
#import src.DB;
#import src.Person
import  mock
import src.MockExample
import src.MockExample
from pytest_mock import mocker
from src.MockExample import DB


def test_save(mocker):
    return mocker.patch.object(DB,'db')

def test_per(test_save):
    gabe=Person("Gabe",test_save)
    gabe.save()
    test_save.persist.assert_called_with(gabe)
