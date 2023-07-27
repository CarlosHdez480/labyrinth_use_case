import pytest

from src.generate_labyrinth import GenerateLabyrinth


@pytest.fixture
def labyrinth_generator():
    return GenerateLabyrinth()


# Test Cases
def test_check_create_base_matrix_with_obstacles_x_dimension(labyrinth_generator):
    dimensions = [10, 5]
    base_matrix = labyrinth_generator.create_labyrinth(dimensions,
                                                       probability_find_obstacle=0.5)

    assert len(base_matrix[0]) == 10


def test_check_create_base_matrix_with_obstacles_y_dimension(labyrinth_generator):
    dimensions = [10, 5]
    base_matrix = labyrinth_generator.create_labyrinth(dimensions,
                                                       probability_find_obstacle=0.5)

    assert len(base_matrix) == 5


def test_check_no_obstacles_symbols(labyrinth_generator):
    dimensions = [10, 5]
    base_matrix_without_obstacles = labyrinth_generator.create_labyrinth(dimensions,
                                                                         base_element_not_obstacle="+",
                                                                         base_element_obstacle="*",
                                                                         probability_find_obstacle=1)
    assert base_matrix_without_obstacles[0][0] == "+"


def test_check_obstacles_symbols(labyrinth_generator):
    dimensions = [10, 5]
    base_matrix_with_obstacles = labyrinth_generator.create_labyrinth(dimensions,
                                                                      base_element_not_obstacle="+",
                                                                      base_element_obstacle="*",
                                                                      probability_find_obstacle=0.0)
    assert base_matrix_with_obstacles[0][0] == "*"
