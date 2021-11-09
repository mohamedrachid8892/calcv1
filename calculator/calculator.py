"""Simple calculator that can perform the basic arithmetic operations"""
from calculator.history.calculations import Calculations


class Calculator:
    """Calculator class for performing simple arithmetic operations"""
    history = []

    @staticmethod
    def get_result_value():
        """Returns the result of the last calculation"""
        return Calculations.get_last_calculation_value()

    @staticmethod
    def add_numbers(tuple_values: tuple):
        """Adds a tuple of numbers"""
        Calculations.add_addition_calculation(tuple_values)
        return True

    @staticmethod
    def subtract_numbers(tuple_values: tuple):
        """Subtracts a tuple of numbers"""
        Calculations.add_subtraction_calculation(tuple_values)
        return True

    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """Multiplies a tuple of numbers"""
        Calculations.add_multiplication_calculation(tuple_values)
        return True

    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """Divides a tuple of numbers"""
        Calculations.add_division_calculation(tuple_values)
        return True
