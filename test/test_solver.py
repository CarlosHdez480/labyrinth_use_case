import pytest

from src.solver import MazeSolver


@pytest.fixture
def solver():
    return MazeSolver()


# Test Cases
def test_check_solver_matrix(solver):
    """Test to check solver labyrinth matrix"""
    matrix = [['0', '0', '0', '1', '1', '1', '0', '0', '1'],
              ['1', '1', '1', '1', '1', '1', '0', '1', '0'],
              ['1', '1', '1', '1', '1', '0', '0', '1', '1'],
              ['1', '1', '1', '0', '1', '1', '1', '1', '1'],
              ['0', '1', '0', '0', '1', '1', '0', '0', '0']]

    min_movements = solver.find_min_movements(matrix,
                                              "0",
                                              "1")
    assert min_movements == -1
