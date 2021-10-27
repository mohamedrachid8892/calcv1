"""Simple calculator that can perform the basic arithmetic operations"""


class Calculator:
    """Calculator class for performing simple arithmetic operations"""
    result = 0

    def get_result(self):
        """Get result of calculations"""
        return self.result

    def add_number(self, other):
        """Adds number to result"""
        self.result = self.result + other
        return self.result

    def subtract_number(self, other):
        """Subtracts number from result"""
        self.result = self.result - other
        return self.result

    def multiply_number(self, other):
        """Multiplies result and other"""
        self.result = self.result * other
        return self.result

    def divide_number(self, other):
        """Divides number by result"""
        if other == 0:
            raise ZeroDivisionError
        self.result = self.result / other
        return self.result
