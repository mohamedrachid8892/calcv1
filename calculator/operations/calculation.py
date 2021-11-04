"""Calculation class"""

class Calculation:
    """Calculation class is used by the calculations to complete their operation"""

    # Default constructor
    def __init__(self, values: tuple):
        self.values = Calculation.convert_args_to_list_float(values)

    @staticmethod
    def convert_args_to_list_float(values):
        """Standardize values to list of floats"""
        list_values_float = []
        for value in values:
            list_values_float.append(float(value))
        return list_values_float
