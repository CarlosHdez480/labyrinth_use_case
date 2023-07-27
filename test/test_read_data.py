import pytest

from src.read_data import ReadData


@pytest.fixture
def reader():
    return ReadData()


# Test Cases
def test_check_read_matrix_from_txt_file_x_dimension(reader):
    """Test to check matrix from txt file x dimension"""
    folder_to_search = "input"
    filename = "example_labyrinth.txt"

    base_matrix = reader.read_matrix_from_txt_file(filename,
                                                   folder_to_search)

    assert len(base_matrix[0]) == 9


def test_check_read_matrix_from_txt_file_y_dimension(reader):
    """Test to check matrix from txt file y dimension"""
    folder_to_search = "input"
    filename = "example_labyrinth.txt"

    base_matrix = reader.read_matrix_from_txt_file(filename,
                                                   folder_to_search)
    assert len(base_matrix) == 5
