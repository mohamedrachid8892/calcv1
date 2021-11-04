"""Simple calculator that can perform the basic arithmetic operations"""
from calculator.operations.add import Addition
from calculator.operations.divide import Division
from calculator.operations.multiply import Multiplication
from calculator.operations.subtract import Subtraction


class Calculator:
    """Calculator class for performing simple arithmetic operations"""
    history = []

    @staticmethod
    def clear_history():
        """Clear the calculation history"""
        Calculator.history.clear()
        return True

    @staticmethod
    def number_of_calculations():
        """Counts the number of calculations in the history"""
        return len(Calculator.history)

    @staticmethod
    def remove_calculation(index):
        """Removes the ith calculation from the history"""
        Calculator.history.pop(index)
        return True

    @staticmethod
    def get_calculation_first():
        """Get a calculation from the history"""
        return Calculator.history[0].get_result()

    @staticmethod
    def get_calculation_last():
        """Get the most recent calculation"""
        return Calculator.history[-1].get_result()

    @staticmethod
    def add_numbers(*args):
        """Adds two numbers together"""
        addition = Addition(args)
        Calculator.history.append(addition)
        return addition.get_result()

    @staticmethod
    def subtract_numbers(*args):
        """Subtracts value_b from value_a"""
        subtraction = Subtraction(args)
        Calculator.history.append(subtraction)
        return subtraction.get_result()

    @staticmethod
    def multiply_numbers(*args):
        """Multiplies two numbers together"""
        multiplication = Multiplication(args)
        Calculator.history.append(multiplication)
        return multiplication.get_result()

    @staticmethod
    def divide_numbers(*args):
        """Divides value_a by value_b"""
        division = Division(args)
        Calculator.history.append(division)
        return division.get_result()
