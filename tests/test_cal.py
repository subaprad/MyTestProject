import pytest;
import src.cal;


def test_sum():
    assert 7 == src.cal.sum(3, 4)

def test_sub():
    assert 2 == src.cal.sub(8, 6)
