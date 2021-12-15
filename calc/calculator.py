"""Simple calc that can perform the basic arithmetic calculations"""
from calc.history.calculations import Calculations


class Calculator:
    """Calculator class for performing simple arithmetic calculations"""

    history = []

    @staticmethod
    def csv_row_to_tuple():
        """Reads in a CSV file to be processed"""

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

    @staticmethod
    def get_history():
        """Returns the history of calculations"""
        return Calculations.history

    # @staticmethod
    # def get_history_from_csv():
    #     """Get history from CSV file"""
    #     return Calculations.readHistoryfromCSV()
    #
    # @staticmethod
    # def write_history_to_csv():
    #     """Write the history to a CSV file"""
    #     return Calculations.writeHistoryToCSV()
