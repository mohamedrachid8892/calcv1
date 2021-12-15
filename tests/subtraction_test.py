"""Testing Subtraction"""
from calc.calculations.subtract import Subtraction


def test_subtraction():
    """Testing the subtraction method"""
    # Arrange
    numbers = (1.0, 2.0)
    # Act
    subtraction = Subtraction(numbers)
    # Assert
    assert subtraction.get_result() == -1
