import random
import copy
import types
import numpy
import pandas

from typing import Optional

from src.Decorators import Decorators
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
        - send_notification(err: Exception, file: str, severity: str, origin Optional[str] = "",
    destination Optional[str] = "", reach Optional[str] = ""): Send notification to slack.
        - get_webhook(config_file: str): Get Webhook of slack.
    """

    def __init__(self,
                 logger: Optional[types.ModuleType] = None):
        """
        Constructs a new GenerateLabyrinth object.

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

        super().__init__(self.logger)

    @Decorators.decorator_write_log_init_end_method
    def __create_base_labyrinth_matrix(self,
                                       dimension_x: int,
                                       dimension_y: int,
                                       base_element_not_obstacle: Optional[str] = ".") -> list:
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
                                                        probability_find_obstacle: Optional[float] = 0.75,
                                                        base_element_obstacle: Optional[str] = "#") -> list:

        base_labyrinth_matrix_with_obstacles = copy.deepcopy(base_labyrinth_matrix[:][:])

        for element_in_y_dimension in range(len(base_labyrinth_matrix)):
            for element_in_x_dimension in range(len(base_labyrinth_matrix[0])):
                if random.random() > probability_find_obstacle:
                    base_labyrinth_matrix_with_obstacles[element_in_y_dimension][
                        element_in_x_dimension] = base_element_obstacle
        return base_labyrinth_matrix_with_obstacles
