"""Testing CSV Handling Functions"""
import os.path
import pandas as pd
from csvmanager.write_csv import WriteCSV
from csvmanager.read_csv import ReadCSV


def test_write_csv():
    """Testing the WriteCSV class"""
    # Arrange
    filename = 'output.csv'
    os.chdir('/home/myuser/tests/data/')
    path = os.getcwd()
    full_path = path + '/' + filename
    name_dict = {
        'value1': ['1.0', '2.0', '3.0', '4.0'],
        'value2': ['1.0', '2.0', '3.0', '4.0'],
        'result': [2.0, 4.0, 6.0, 8.0]
    }
    # Remove the current output.csv file
    os.remove(full_path)
    data_frame = pd.DataFrame(name_dict)
    # Act
    WriteCSV.data_frame_to_csv(full_path, data_frame)
    # Assert
    assert os.path.exists(full_path)


def test_read_csv():
    """Testing the ReadCSV class"""
    # Arrange
    filename = 'output.csv'
    os.chdir('/home/myuser/tests/data/')
    path = os.getcwd()
    full_path = path + '/' + filename
    # Act
    data_frame = ReadCSV.data_frame_from_csv(full_path)
    # Assert
    assert isinstance(data_frame, pd.DataFrame)
