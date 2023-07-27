"""maze solver"""

from collections import deque

from src.logger import Logger
from src.decorators import Decorators


class MazeSolver:
    """
           A class to sort out labyrinth problem.

           ...

           Attributes
           ----------
               - logger (logging): The log file.

           Methods
           -------
               - question_matrix_dimensions(): Ask user by dimensions of matrix.
               - question_probability_obstacles(): Ask user probability of obstacles.
               - question_symbol_corridors(): Ask user symbol of corridors,
               space without obstacles.
               - question_symbol_obstacles(): Ask user symbol of obstacles,
               space with obstacles.
               - initial_question_user_method_input_labyrinth(): Ask user input data
               of labyrinth matrix.
           """

    def __init__(self,
                 logger=None):
        """
        Constructs a MazeSolver object.

        ...

        Parameters
        ----------
            :param : logger file.
            :type logger: logging
        """
        if logger is None:
            logger_object = Logger("foo test")
            logger = logger_object.create_logger_file("foo test")
        self.logger = logger

    @Decorators.decorator_write_log_init_end_method
    def find_min_movements(self,
                           matrix: list,
                           space_symbol: str,
                           obstacle_symbol: str):
        """
        read matrix from txt.

        ...

        Parameters
        ----------
            :param matrix: file name where matrix it is in.
            :type matrix: str
            :param space_symbol: symbol on labyrinth of free space.
            :type space_symbol: str
            :param obstacle_symbol: symbol on labyrinth of walls.
            :type obstacle_symbol: str
        """

        def bfs(x_matrix_dimension: int,
                y_matrix_dimension: int,
                orientation: str):
            visited = set()
            queue = deque([(x_matrix_dimension,
                            y_matrix_dimension,
                            orientation)])
            moves = 0

            while queue:
                for _ in range(len(queue)):
                    x_matrix_dimension, y_matrix_dimension, orientation = queue.popleft()

                    if (x_matrix_dimension, y_matrix_dimension, orientation) == (n_dimension - 1,
                                                                                 m_dimension - 1,
                                                                                 "horizontal"):
                        return moves

                    if (x_matrix_dimension, y_matrix_dimension, orientation) not in visited:
                        visited.add((x_matrix_dimension,
                                     y_matrix_dimension,
                                     orientation))
                        neighbours = self.__get_neighbours(matrix,
                                                           x_matrix_dimension,
                                                           y_matrix_dimension,
                                                           orientation,
                                                           obstacle_symbol,
                                                           space_symbol)
                        queue.extend(neighbours)

                moves += 1

            return -1  # If no path is found

        n_dimension, m_dimension = len(matrix), len(matrix[0])
        return bfs(0, 0, "horizontal")

    @Decorators.decorator_write_log_init_end_method
    def __is_valid_move(self,
                        matrix: list,
                        x_dimension: int,
                        y_dimension: int,
                        orientation: str,
                        obstacle_symbol: str,
                        space_symbol: str):

        """Function to check if it is a valid move"""
        n_dimension, m_dimension = len(matrix), len(matrix[0])

        if x_dimension < 0 \
                or x_dimension + 2 >= n_dimension \
                or y_dimension < 0\
                or y_dimension + 2 >= m_dimension:
            return False
        for i in range(x_dimension, x_dimension + 3):
            for j in range(y_dimension, y_dimension + 3):
                if matrix[i][j] == obstacle_symbol:
                    return False

        if orientation == "horizontal":
            return matrix[x_dimension + 1][y_dimension] == space_symbol \
                   and matrix[x_dimension + 1][y_dimension + 1] == space_symbol \
                   and matrix[x_dimension + 1][
                       y_dimension + 2] == space_symbol
        if orientation == "vertical":
            return matrix[x_dimension][y_dimension + 1] == space_symbol \
                   and matrix[x_dimension + 1][y_dimension + 1] == space_symbol \
                   and matrix[x_dimension + 2][
                       y_dimension + 1] == space_symbol
        raise ValueError("Invalid orientation")

    @Decorators.decorator_write_log_init_end_method
    def __get_neighbours(self,
                         matrix: list,
                         x_dimension: int,
                         y_refactor: int,
                         orientation: str,
                         obstacle_symbol: str,
                         space_symbol: str):
        """Function to get surrounded cells in labyrinth space"""
        neighbours = []
        if self.__is_valid_move(matrix,
                                x_dimension - 1,
                                y_refactor,
                                "horizontal",
                                obstacle_symbol,
                                space_symbol):
            neighbours.append((x_dimension - 1,
                               y_refactor,
                               "horizontal"))
        if self.__is_valid_move(matrix,
                                x_dimension + 1,
                                y_refactor,
                                "horizontal",
                                obstacle_symbol,
                                space_symbol):
            neighbours.append((x_dimension + 1,
                               y_refactor,
                               "horizontal"))
        if self.__is_valid_move(matrix,
                                x_dimension,
                                y_refactor - 1,
                                "vertical",
                                obstacle_symbol,
                                space_symbol):
            neighbours.append((x_dimension,
                               y_refactor - 1,
                               "vertical"))
        if self.__is_valid_move(matrix,
                                x_dimension,
                                y_refactor + 1,
                                "vertical",
                                obstacle_symbol,
                                space_symbol):
            neighbours.append((x_dimension,
                               y_refactor + 1,
                               "vertical"))

        if orientation == "horizontal":
            if self.__is_valid_move(matrix,
                                    x_dimension,
                                    y_refactor,
                                    "vertical",
                                    obstacle_symbol,
                                    space_symbol):
                neighbours.append((x_dimension,
                                   y_refactor,
                                   "vertical"))
            if self.__is_valid_move(matrix,
                                    x_dimension + 2,
                                    y_refactor,
                                    "vertical",
                                    obstacle_symbol,
                                    space_symbol):
                neighbours.append((x_dimension + 2,
                                   y_refactor,
                                   "vertical"))
        elif orientation == "vertical":
            if self.__is_valid_move(matrix,
                                    x_dimension,
                                    y_refactor,
                                    "horizontal",
                                    obstacle_symbol,
                                    space_symbol):
                neighbours.append((x_dimension,
                                   y_refactor,
                                   "horizontal"))
            if self.__is_valid_move(matrix,
                                    x_dimension,
                                    y_refactor + 2,
                                    "horizontal",
                                    obstacle_symbol,
                                    space_symbol):
                neighbours.append((x_dimension,
                                   y_refactor + 2,
                                   "horizontal"))
        return neighbours
