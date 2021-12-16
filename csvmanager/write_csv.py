"""Class that handles writing dataframes to CSV files"""
import os


class WriteCSV:
    """Write dataframes to CSV files"""

    @staticmethod
    def data_frame_to_csv(data_frame):
        """Take a dataframe, df, and write it to a CSV file, filename"""
        return data_frame.to_csv('/../results/results.csv',
                                 float_format='%.2f',
                                 index=False,
                                 header=False)
