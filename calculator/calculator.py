"""Simple calculator that can perform the basic arithmetic operations"""
from calculator.operations.add import Addition
from calculator.operations.divide import Division
from calculator.operations.multiply import Multiplication
from calculator.operations.subtract import Subtraction

class Calculator:
    """Calculator class for performing simple arithmetic operations"""
    calculation = list

    @staticmethod
    def add_number(value_a, value_b):
        """Adds two numbers together"""
        return Addition.add(value_a, value_b)

    @staticmethod
    def subtract_number(value_a, value_b):
        """Subtracts value_b from value_a"""
        return Subtraction.subtract(value_a, value_b)

    @staticmethod
    def multiply_number(value_a, value_b):
        """Multiplies two numbers together"""
        return Multiplication.multiply(value_a, value_b)

    @staticmethod
    def divide_number(value_a, value_b):
        """Divides value_a by value_b"""
        return Division.divide(value_a, value_b)
