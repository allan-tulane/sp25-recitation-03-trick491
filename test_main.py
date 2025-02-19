from main import BinaryNumber, quadratic_multiply
import pytest



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(9), BinaryNumber(9)) == 9*9
    assert quadratic_multiply(BinaryNumber(12), BinaryNumber(12)) == 12*12
    assert quadratic_multiply(BinaryNumber(60), BinaryNumber(6)) == 360
    assert quadratic_multiply(BinaryNumber(100), BinaryNumber(120)) == 12000
    assert quadratic_multiply(BinaryNumber(50), BinaryNumber(50)) == 2500
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(4)) == 4
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(1)) == 2

