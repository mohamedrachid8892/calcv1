"""Class that handles writing dataframes to CSV files"""
import os


class WriteCSV:
    """Write dataframes to CSV files"""

    @staticmethod
    def data_frame_to_csv(filename, data_frame):
        """Take a dataframe, df, and write it to a CSV file, filename"""
        print(os.path.abspath(filename))
        return data_frame.to_csv(os.path.abspath(filename),
                                 float_format='%.2f',
                                 index=True,
                                 header=True)
