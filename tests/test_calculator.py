"""Testing the Calculator"""
import pytest
from calculator.calculator import Calculator

@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculator.clear_history()

#You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_numbers(1.0,2.0,3.0) == 6.0

def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.subtract_numbers(1.0,2.0,3.0) == -4.0

def test_calculator_multiply_static(clear_history_fixture):
    """Testing the multiply method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.multiply_numbers(1.0,2.0,2.0,2.0) == 8.0

def test_calculator_divide_static(clear_history_fixture):
    """Testing the divide method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.divide_numbers(16.0,4.0,2.0,2.0) == 1.0

def test_calculator_division_by_zero(clear_history_fixture):
    """Testing the division by zero handling of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.divide_numbers(8.0,2.0, 0.0) == ZeroDivisionError

def test_calculator_history_static_property(clear_history_fixture):
    """Testing the calculations are added to the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    Calculator.add_numbers(1.0,2.0)
    Calculator.add_numbers(2.0,2.0)
    assert len(Calculator.history) == 2

def test_calculator_length(clear_history_fixture):
    """Testing the counting of number of calculations"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    Calculator.add_numbers(2.0,2.0)
    Calculator.add_numbers(2.0,2.0)
    Calculator.add_numbers(2.0,2.0)
    assert Calculator.number_of_calculations() == 3

def test_remove_calculation(clear_history_fixture):
    """Testing the removal of of calculations"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    Calculator.add_numbers(1.0,2.0)
    assert Calculator.remove_calculation(0) == True

def test_clear_history():
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    Calculator.add_numbers(1.0,2.0)
    assert Calculator.clear_history() == True


def test_get_calculation_first(clear_history_fixture):
    """Testing getting the first calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    Calculator.add_numbers(1.0,2.0)
    Calculator.multiply_numbers(4.0,2.0,6.0)
    Calculator.divide_numbers(0.0,2.0)
    assert Calculator.get_calculation_first() == 3

def test_get_calculation_last(clear_history_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    Calculator.add_numbers(1.0,2.0)
    Calculator.multiply_numbers(4.0,2.0,6.0)
    Calculator.divide_numbers(0.0,2.0)
    assert Calculator.get_calculation_last() == 0
