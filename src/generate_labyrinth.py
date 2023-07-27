import random
import copy

from typing import Optional

from src.decorators import Decorators
from src.Logger import Logger


class GenerateLabyrinth:
    """
    A class to generate initial labyrinth.

    ...

    Attributes
    ----------
        - logger (logging): The log file.

    Methods
    -------
        - create_labyrinth(dimensions: list, base_element_not_obstacle: Optional[str] = ".",
        base_element_obstacle: Optional[str] = "#", probability_find_obstacle: Optional[float] = 0.75):
        create labyrinth initial matrix.
    """

    def __init__(self,
                 logger=None):
        """
        Constructs a GenerateLabyrinth object.

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
    @Decorators.decorator_execution_time
    def create_labyrinth(self,
                         dimensions: list,
                         base_element_not_obstacle: Optional[str] = ".",
                         base_element_obstacle: Optional[str] = "#",
                         probability_find_obstacle: Optional[float] = 0.75,
                         ):
        """
        Create base labyrinth matrix

        ...

        Parameters
        ----------
            :param dimensions: dimensions of labyrinth matrix.
            :type dimensions: list
            :param base_element_not_obstacle: symbol to represent corridors.
            :type base_element_not_obstacle: str
            :param base_element_obstacle: symbol to represent obstacles.
            :type base_element_obstacle: str
            :param probability_find_obstacle: probability a cell it is an obstacle.
            :type probability_find_obstacle: float
            :return: a dictionary sorted with hotel data.
            :rtype: dict
        """

        dimension_x = dimensions[0]
        dimension_y = dimensions[1]

        base_labyrinth_matrix = self.__create_base_labyrinth_matrix(dimension_x,
                                                                    dimension_y,
                                                                    base_element_not_obstacle)

        base_labyrinth_matrix_with_obstacles = self.__create_obstacles_inside_base_labyrinth_matrix(
            base_labyrinth_matrix,
            base_element_obstacle,
            probability_find_obstacle,
        )
        return base_labyrinth_matrix_with_obstacles

    @Decorators.decorator_write_log_init_end_method
    def __create_base_labyrinth_matrix(self,
                                       dimension_x: int,
                                       dimension_y: int,
                                       base_element_not_obstacle) -> list:
        base_matrix_labyrinth = []
        for element_in_y_dimension in range(dimension_y):
            row = []
            for element_in_x_dimension in range(dimension_x):
                row.append(base_element_not_obstacle)
            base_matrix_labyrinth.append(row)
        return base_matrix_labyrinth

    @Decorators.decorator_write_log_init_end_method
    def __create_obstacles_inside_base_labyrinth_matrix(self,
                                                        base_labyrinth_matrix: list,
                                                        base_element_obstacle: str,
                                                        probability_find_obstacle: float,
                                                        ) -> list:

        base_labyrinth_matrix_with_obstacles = copy.deepcopy(base_labyrinth_matrix[:][:])

        for element_in_y_dimension in range(len(base_labyrinth_matrix)):
            for element_in_x_dimension in range(len(base_labyrinth_matrix[0])):
                if random.random() > probability_find_obstacle:
                    base_labyrinth_matrix_with_obstacles[element_in_y_dimension][
                        element_in_x_dimension] = base_element_obstacle
        return base_labyrinth_matrix_with_obstacles
