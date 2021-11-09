"""Testing Subtraction"""
from calculator.operations.subtract import Subtraction

def test_subtraction():
    """Testing the subtraction method"""
    numbers = (1.0, 2.0)
    subtraction = Subtraction(numbers)
    assert subtraction.get_result() == -1
