"""Division Class"""
from calculator.operations.calculation import Calculation

class Division(Calculation):
    """Division Class"""

    def get_result(self):
        """Divide numbers to get the quotient, checking if the divisor is 0"""

        quotient_of_values = self.values[0]
        for value in self.values[1:]:
            if value == 0:
                return ZeroDivisionError
            quotient_of_values = quotient_of_values / value
        return quotient_of_values
