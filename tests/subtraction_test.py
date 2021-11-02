"""Testing Subtraction"""
from calculator.operations.subtract import Subtraction

def test_subtraction():
    """Testing the subtraction method"""
    assert Subtraction.subtract(1, 2) == -1
