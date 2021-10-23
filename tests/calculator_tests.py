"""Testing the Calculator"""
from calculator.main import Calculator


def test_calculator_result():
    """Testing Calculator constructor"""
    calc = Calculator()
    assert calc.result == 0


def test_calculator_add():
    """Testing the Add function of the calculator"""
    calc = Calculator()
    calc.add_number(4)
    assert calc.result == 4


def test_calculator_subtract():
    """Testing the Subtract function of the calculator"""
    calc = Calculator()
    calc.subtract_number(1)
    assert calc.result == -1


def test_calculator_multiply():
    """Testing the Multiply function of the calculator"""
    calc = Calculator()
    calc.add_number(1)
    calc.multiply_number(2)
    assert calc.result == 2


def test_calculator_division():
    """Testing the division function of the calculator"""
    calc = Calculator()
    calc.add_number(4)
    calc.divide_number(2)
    assert calc.result == 2


def test_calculator_division_by_zero():
    """Testing the divide function of the calculator when dividing by zero"""
    calc = Calculator()
    calc.divide_number(0)
    assert ZeroDivisionError, "You can't divide by 0."
