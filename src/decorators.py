"""module with decorators"""

import time
import types

from typing import Optional
from functools import wraps

from src.logger import Logger


class Decorators:
    """
    Class representing a Decorators generics.
    ...

    Attributes
    ----------
        - logger (logging): The log file.

    Methods
    -------
    - __init__(logger: logging): Constructs a new Decorators Class object with the given log file.
    """

    def __init__(self,
                 logger: Optional[types.ModuleType] = None):
        """
        Constructs a new Decorators object.

         ...

        Parameters
        ----------
            :param logger: logger file.
            :type logger: logging
        """
        # set logger
        if logger is None:
            logger_object = Logger("foo test")
            logger = logger_object.create_logger_file("foo test")
        self.logger = logger

    @staticmethod
    def decorator_execution_time(method):
        """Decorator write execution time, function lasting"""
        wraps(method)

        def method_wrapped(self,
                           *args,
                           **kwargs):
            start_time = time.time()
            name_method = method.__name__.replace("_",
                                                  " ")
            method_result = method(self,
                                   *args,
                                   **kwargs)
            time_stamp = time.time() - start_time
            try:
                self.logger.info(f"[{name_method}] execution time --- {time_stamp} seconds ---")
            except AttributeError:
                self.info(f"[{name_method}] execution time --- {time_stamp} seconds ---")
            return method_result
        return method_wrapped

    @staticmethod
    def decorator_write_log_init_end_method(method):
        """Decorator write when function starts and finish"""
        wraps(method)

        def method_wrapped(self,
                           *args,
                           **kwargs):
            name_method = method.__name__.replace("_",
                                                  " ")
            try:
                self.logger.info(f"[{name_method}] init of method {name_method}: STARTING")
            except AttributeError:
                self.info(f"[{name_method}] init of method {name_method}: STARTING")

            method_result = method(self,
                                   *args,
                                   **kwargs)

            try:
                self.logger.info(f"[{name_method}] execution of method {name_method}: OK")
            except AttributeError:
                self.info(f"[{name_method}] execution of method {name_method}: OK")

            return method_result
        return method_wrapped


if __name__ == "__main__":
    # mock run
    decorators_object = Decorators()


    @decorators_object.decorator_execution_time
    def add_values(*args):
        """Sum values"""
        result_sum = 0
        for value_to_sum in args[1:]:
            result_sum += value_to_sum
        return result_sum


    ADDED = add_values(decorators_object.logger,
                       5,
                       6)
