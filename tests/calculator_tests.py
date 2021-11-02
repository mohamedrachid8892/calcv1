"""Testing the Calculator"""
from calculator.calculator import Calculator

def test_calculator_add():
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(1, 1) == 2


def test_calculator_subtract():
    """Testing the Subtract function of the calculator"""
    assert Calculator.subtract_number(1, 2) == -1


def test_calculator_multiply():
    """Testing the Multiply function of the calculator"""
    assert Calculator.multiply_number(2, 2) == 4


def test_calculator_division():
    """Testing the division function of the calculator"""
    assert Calculator.divide_number(6, 3) == 2


def test_calculator_division_by_zero():
    """Testing the divide function of the calculator when dividing by zero"""
    assert Calculator.divide_number(4, 0) == ZeroDivisionError
