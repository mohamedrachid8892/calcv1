"""Calculations History Class"""
from calculator.operations.add import Addition
from calculator.operations.divide import Division
from calculator.operations.multiply import Multiplication
from calculator.operations.subtract import Subtraction

class Calculations:
    """"Calculations class manages the history of calculations"""

    history = []

    @staticmethod
    def clear_history():
        """Clear the history of calculations"""
        Calculations.history.clear()
        return True

    @staticmethod
    def calculations_count():
        """Get the number of calculations in history"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation_object():
        """Return the last calculation object"""
        return Calculations.history[-1]

    @staticmethod
    def get_last_calculation_value():
        """Get the last calculation value"""
        return Calculations.history[-1].get_result()

    @staticmethod
    def get_first_calculation_object():
        """Get first calculation object"""
        return Calculations.history[0]

    @staticmethod
    def get_calculation(num):
        """Return any calculation from history"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """Add a calculation to history"""
        return Calculations.history.append(calculation)

    @staticmethod
    def add_addition_calculation(values):
        """Add addition object to history using factory method create"""
        Calculations.add_calculation(Addition.create(values))
        return True

    @staticmethod
    def add_subtraction_calculation(values):
        """Add subtraction object to history using factory method create"""
        Calculations.add_calculation(Subtraction.create(values))
        return True

    @staticmethod
    def add_multiplication_calculation(values):
        """Add multiplication object to history using factory method create"""
        Calculations.add_calculation(Multiplication.create(values))
        return True

    @staticmethod
    def add_division_calculation(values):
        """Add division object to history using factory method create"""
        Calculations.add_calculation(Division.create(values))
        return True
