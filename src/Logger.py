"""
Logger.

to manage logger file.
"""
import sys
import os
import datetime
import logging
import types

from typing import Optional


class Logger:
    """
    Class representing logger file.

    ...

    Attributes
    ----------
        - log_name (str): The log file name .

    Methods
    -------
        - create_logger_file(log_name: str, process_name: str, create_directory: Optional[bool] = False):
        Allow create logger file from class object.
    """

    def __init__(self,
                 log_name: str):
        """
        Constructs a new Logger object setting paths.

        ...

        Parameters
        ----------
            :param log_name: The name of logger file.
            :type log_name: str
        """
        __WORK_DIR = os.path.abspath(os.path.dirname(__file__))
        __COMMON_DIR = os.path.abspath(os.path.join(__WORK_DIR,
                                                    '..'))
        # set paths
        sys.path.append(__WORK_DIR)
        sys.path.append(__COMMON_DIR)

        # filename log, to create log
        self.__directory_log = __COMMON_DIR + "/logs"
        self.filename_log = self.__directory_log + f"/{log_name}.log"

    def create_logger_file(self,
                           process_name: str,
                           create_directory: Optional[bool] = False) -> types.ModuleType:
        """
        Create a new log file.

        ...

        Parameters
        ----------
            :param process_name: The name of the process where logs are written down.
            :type process_name: str
            :param create_directory: If is necessary create a new directory or not.
            :type create_directory: bool
            :return: A logging file to write down logs info.
            :rtype: types.ModuleType
        """
        # create directory if it´s necessary
        if create_directory:
            os.mkdir(self.__directory_log)

        # each three days remove logs
        if (datetime.datetime.now().weekday()) % 3 == 0:
            try:
                os.remove(self.filename_log)
            except Exception as err:
                print(f"file doesn´t exist, not needed remove actions: {err}")
        # create logger file
        try:
            logging.basicConfig(filename=self.filename_log,
                                format='%(asctime)s p%(process)s {%(pathname)s:%(lineno)d}  -- %(levelname)s:  %('
                                       'message)s',
                                level=logging.INFO)
        except Exception as err:
            print(err)
            os.mkdir(self.__directory_log)
            logging.basicConfig(filename=self.filename_log,
                                format='%(asctime)s p%(process)s {%(pathname)s:%(lineno)d}  -- %(levelname)s:  %('
                                       'message)s',
                                level=logging.INFO)
        logging.info(
            f"\n\n starting {process_name} process date {datetime.datetime.now().date()}\n========================="
            f"=====================================================================\n\n")
        return logging
