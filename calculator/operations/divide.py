"""Division Class"""

class Division:
    """Division Class"""

    @staticmethod
    def divide(value_a, value_b):
        """Divide two numbers together, checking if the divisor is 0"""
        if value_b == 0:
            return ZeroDivisionError
        return value_a / value_b
