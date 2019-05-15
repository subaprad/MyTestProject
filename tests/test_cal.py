import pytest;
import src.cal;


def test_sum():
    assert 7 == src.cal.sum(3, 4)
