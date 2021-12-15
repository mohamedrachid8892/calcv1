"""Testing Addition"""
from calc.calculations.add import Addition


def test_addition():
    """Testing addition"""

    # Arrange
    numbers = (1.0, 2.0, 3.0)
    # Act
    addition = Addition(numbers)
    # Assert
    assert addition.get_result() == 6.0
