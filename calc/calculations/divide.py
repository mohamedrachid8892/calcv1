"""Division Class"""
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """Division Class"""

    def get_result(self):
        """Divide numbers to get the quotient, checking if the divisor is 0"""

        quotient_of_values = self.values[0]
        for value in self.values[1:]:
            try:
                quotient_of_values = quotient_of_values / value
            except ZeroDivisionError as zero_division_error:
                raise ZeroDivisionError from zero_division_error
        return quotient_of_values
