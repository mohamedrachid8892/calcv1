"""Multiplication Class"""
from calc.calculations.calculation import Calculation


class Multiplication(Calculation):
    """Multiplication Class"""

    def get_result(self):
        """Multiply method to get the product of numbers"""

        product_of_values = 1.0
        for value in self.values:
            product_of_values = value * product_of_values
        return product_of_values
