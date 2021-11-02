"""Testing Multiplication"""
from calculator.operations.multiply import Multiplication

def test_multiplication():
    """Testing the multiplication method"""
    assert Multiplication.multiply(2, 2) == 4
