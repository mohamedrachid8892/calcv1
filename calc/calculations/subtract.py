"""Subtraction Class"""
from calc.calculations.calculation import Calculation


class Subtraction(Calculation):
    """Subtraction Class"""

    operation = "subtraction"

    def get_result(self):
        """Subtract method to get the difference of numbers"""

        difference_of_values = self.values[0]
        # print(self.values[0])
        for value in self.values[1:]:
            difference_of_values = difference_of_values - value
        return difference_of_values
