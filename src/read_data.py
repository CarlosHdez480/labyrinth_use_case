"""module to read data"""

import os

from src.logger import Logger


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
        Constructs a QuestionsUsers object.

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

    def read_matrix_from_txt_file(self,
                                  filename: str,
                                  folder: str):
        try:
            with open(f"{self.__common_dir}/{folder}/" + filename) as f:
                labyrinth_matrix = [x.rstrip("\n").split(" ") for x in f.readlines()]
            f.close()
            return labyrinth_matrix
        except Exception as err:
            self.logger.error(f"[read txt file] not possible open file, err: {err}")
            return []
