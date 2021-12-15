"""Class to handle reading CSV files using Pandas"""
import os
import pandas as pd


class ReadCSV:
    """Class that handles reading CSV files using Pandas"""

    @staticmethod
    def data_frame_from_csv(filename):
        """Create a Pandas dataframe from an input CSV file"""
        return pd.read_csv(os.path.abspath(filename))
