"""Testing Addition"""
from calculator.operations.add import Addition

def test_addition():
    """Testing addition"""
    numbers = (1.0, 2.0)
    addition = Addition(numbers)
    assert addition.get_result() == 3.0
