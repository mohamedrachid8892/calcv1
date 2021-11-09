"""Testing Multiplication"""
from calculator.operations.multiply import Multiplication

def test_multiplication():
    """Testing the multiplication method"""
    numbers = (2.0, 4.0)
    multiplication = Multiplication(numbers)
    assert multiplication.get_result() == 8
