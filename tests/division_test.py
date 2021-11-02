"""Testing Division"""
from calculator.operations.divide import Division

def test_division():
    """Testing the division method for non-zero arguments"""
    assert Division.divide(6, 2) == 3

def test_addition_by_zero():
    """Testing the case where you divide by zero"""
    assert Division.divide(1, 0) == ZeroDivisionError
