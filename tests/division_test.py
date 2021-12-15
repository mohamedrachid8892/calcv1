"""Testing Division"""
import pytest
from calc.calculations.divide import Division


def test_division():
    """Testing the division method for non-zero arguments"""
    numbers = (4.0, 2.0)
    division = Division(numbers)
    assert division.get_result() == 2


def test_division_by_zero():
    """Testing the case where you divide by zero"""
    numbers = (4, 0)
    with pytest.raises(ZeroDivisionError):
        division = Division(numbers)
        print(division.get_result())
