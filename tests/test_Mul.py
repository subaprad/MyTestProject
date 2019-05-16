import pytest;
import src.Mul;
def test_mul():
    assert src.Mul.mul(2,3)==6;

def test_muln():
    assert src.Mul.mul(3,4)==12;
