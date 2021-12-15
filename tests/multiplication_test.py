"""Testing Multiplication"""
from calc.calculations.multiply import Multiplication


def test_multiplication():
    """Testing the multiplication method"""
    # Arrange
    numbers = (2.0, 4.0)
    # Act
    multiplication = Multiplication(numbers)
    # Assert
    assert multiplication.get_result() == 8
