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
        def bfs(x: int,
                y: int,
                orientation: str):
            visited = set()
            queue = deque([(x,
                            y,
                            orientation)])
            moves = 0

            while queue:
                for _ in range(len(queue)):
                    x, y, orientation = queue.popleft()

                    if (x, y, orientation) == (n - 1, m - 1, "horizontal"):
                        return moves

                    if (x, y, orientation) not in visited:
                        visited.add((x, y, orientation))
                        neighbours = self.__get_neighbours(matrix, x, y,
                                                           orientation,
                                                           obstacle_symbol,
                                                           space_symbol)
                        queue.extend(neighbours)

                moves += 1

            return -1  # If no path is found

        n, m = len(matrix), len(matrix[0])
        return bfs(0, 0, "horizontal")

    @Decorators.decorator_write_log_init_end_method
    def __is_valid_move(self,
                        matrix: list,
                        x: int,
                        y: int,
                        orientation: str,
                        obstacle_symbol: str,
                        space_symbol: str):

        """Function to check if it is a valid move"""
        n, m = len(matrix), len(matrix[0])

        if x < 0 or x + 2 >= n or y < 0 or y + 2 >= m:
            return False
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if matrix[i][j] == obstacle_symbol:
                    return False

        if orientation == "horizontal":
            return matrix[x + 1][y] == space_symbol and matrix[x + 1][y + 1] == space_symbol and matrix[x + 1][
                y + 2] == space_symbol
        elif orientation == "vertical":
            return matrix[x][y + 1] == space_symbol and matrix[x + 1][y + 1] == space_symbol and matrix[x + 2][
                y + 1] == space_symbol
        else:
            raise ValueError("Invalid orientation")

    @Decorators.decorator_write_log_init_end_method
    def __get_neighbours(self,
                         matrix: list,
                         x: int,
                         y: int,
                         orientation: str,
                         obstacle_symbol: str,
                         space_symbol: str):
        """Function to get surrounded cells in labyrinth space"""
        neighbours = []
        if self.__is_valid_move(matrix,
                                x - 1,
                                y,
                                "horizontal",
                                obstacle_symbol,
                                space_symbol):
            neighbours.append((x - 1,
                               y,
                               "horizontal"))
        if self.__is_valid_move(matrix,
                                x + 1,
                                y,
                                "horizontal",
                                obstacle_symbol,
                                space_symbol):
            neighbours.append((x + 1, y, "horizontal"))
        if self.__is_valid_move(matrix,
                                x,
                                y - 1,
                                "vertical",
                                obstacle_symbol,
                                space_symbol):
            neighbours.append((x,
                               y - 1,
                               "vertical"))
        if self.__is_valid_move(matrix,
                                x,
                                y + 1,
                                "vertical",
                                obstacle_symbol,
                                space_symbol):
            neighbours.append((x,
                               y + 1,
                               "vertical"))

        if orientation == "horizontal":
            if self.__is_valid_move(matrix,
                                    x,
                                    y,
                                    "vertical",
                                    obstacle_symbol,
                                    space_symbol):
                neighbours.append((x,
                                   y,
                                   "vertical"))
            if self.__is_valid_move(matrix,
                                    x + 2,
                                    y,
                                    "vertical",
                                    obstacle_symbol,
                                    space_symbol):
                neighbours.append((x + 2,
                                   y,
                                   "vertical"))
        elif orientation == "vertical":
            if self.__is_valid_move(matrix,
                                    x,
                                    y,
                                    "horizontal",
                                    obstacle_symbol,
                                    space_symbol):
                neighbours.append((x,
                                   y,
                                   "horizontal"))
            if self.__is_valid_move(matrix,
                                    x,
                                    y + 2,
                                    "horizontal",
                                    obstacle_symbol,
                                    space_symbol):
                neighbours.append((x,
                                   y + 2,
                                   "horizontal"))
        return neighbours
