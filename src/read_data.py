"""module to read data"""

import os

from src.logger import Logger
from src.decorators import Decorators


class ReadData:
    """
        Read files.

        ...

        Attributes
        ----------
            - logger (logging): The log file.

        Methods
        -------
            - read_txt_file(filename): read txt file.
        """

    def __init__(self,
                 logger=None):
        """
        Constructs a ReadData object.

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

        __work_dir = os.path.abspath(os.path.dirname(__file__))
        self.__common_dir = os.path.abspath(os.path.join(__work_dir,
                                                         '..'))

    @Decorators.decorator_write_log_init_end_method
    def read_matrix_from_txt_file(self,
                                  filename: str,
                                  folder: str) -> list:
        """
        read matrix from txt.

        ...

        Parameters
        ----------
            :param filename: file name where matrix it is in.
            :type filename: str
            :param folder: folder where search file.
            :type folder: str
            :return: a matrix with labyrinth.
            :rtype: list
        """
        try:
            with open(f"{self.__common_dir}/{folder}/" + filename,
                      encoding="utf-8") as file_opened:
                labyrinth_matrix = [x.rstrip("\n").split(" ") for x in file_opened.readlines()]
            file_opened.close()
            return labyrinth_matrix
        except Exception as err:
            self.logger.error(f"[read txt file] not possible open file, err: {err}")
            return []
