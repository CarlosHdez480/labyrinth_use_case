import os

from src.Decorators import Decorators
from src.Logger import Logger


class QuestionsUsers:
    """
        A class to ask user how to input data, and requests some parameters.

        ...

        Attributes
        ----------
            - logger (logging): The log file.

        Methods
        -------
            - question_matrix_dimensions(): Ask user by dimensions of matrix.
            - question_probability_obstacles(): Ask user probability of obstacles.
            - question_symbol_corridors(): Ask user symbol of corridors, space without obstacles.
            - question_symbol_obstacles(): Ask user symbol of obstacles, space with obstacles.
            - initial_question_user_method_input_labyrinth(): Ask user input data of labyrinth matrix.
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

    @Decorators.decorator_write_log_init_end_method
    def question_matrix_dimensions(self) -> list:
        while True:
            dimensions_matrix = input("\nIndicate labyrinth dimensions labyrinth (x, y): \n")
            msg_dimensions_error = "\n\nIncorrect dimensions, please enter values properly, numeric values" \
                                   " separated by comma, for instance [5, 6] \nrestrictions 3 ≤ dimension_x ≤ 1000," \
                                   "3 ≤ dimension_y ≤ 1000"
            try:
                dimensions_matrix_x = dimensions_matrix.split(",")[0].replace("[",
                                                                              "").strip()
                dimensions_matrix_y = dimensions_matrix.split(",")[1].replace("]",
                                                                              "").strip()
                try:
                    dimensions_matrix_x_int = int(dimensions_matrix_x)
                    dimensions_matrix_y_int = int(dimensions_matrix_y)
                    if ((dimensions_matrix_x_int >= 3) & (dimensions_matrix_x_int <= 1000)) & \
                            ((dimensions_matrix_y_int >= 3) & (dimensions_matrix_y_int <= 1000)):
                        return [dimensions_matrix_x_int, dimensions_matrix_y_int]
                    else:
                        print("Not constrains accomplished. " + msg_dimensions_error)
                except ValueError as err:
                    self.logger.warning(f"[question matrix dimensions] not numeric value, value error: {err}")
                    print("Not numeric value. " + msg_dimensions_error)
            except ValueError as err:
                self.logger.warning(f"[question matrix dimensions] not numeric value, value error: {err}")
                print("Not numeric value. " + msg_dimensions_error)
            except IndexError as err:
                self.logger.warning(f"[question matrix dimensions] not indicated dimensions properly, "
                                    f"index error: {err}")
                print("Not indicated dimensions properly " + msg_dimensions_error)

    @Decorators.decorator_write_log_init_end_method
    def question_probability_obstacles(self) -> float:
        while True:
            probability_find_obstacle_input = input("\nIndicate probability find obstacle "
                                                    "[numeric value amongst 0 - 1]: \n")
            msg_probability_error = "\n\nIncorrect probability, value error, please enter values properly [value " \
                                    "amongst " \
                                    "0 - 1] "
            try:
                probability_find_obstacle = float(probability_find_obstacle_input)
                if (probability_find_obstacle > 0) & (probability_find_obstacle < 1):
                    return probability_find_obstacle
                else:
                    print(msg_probability_error)
            except ValueError as err:
                self.logger.warning(f"[question probability obstacles] not indicated probability properly, "
                                    f"value error: {err}")
                print(msg_probability_error)

    @Decorators.decorator_write_log_init_end_method
    def question_symbol_corridors(self) -> str:
        while True:
            agree_corridors_symbol = input("Corridors are represents with '.', are you agree [Y, N]: \n")
            if agree_corridors_symbol == "Y":
                return "."
            elif agree_corridors_symbol == "N":
                base_element_not_obstacle = input("Please enter corridor symbol to use in labyrinth: \n")
                return base_element_not_obstacle
            else:
                self.logger.warning(f"[question symbol corridors] incorrect question option, "
                                    f"input : {agree_corridors_symbol}")
                print("Incorrect option, please enter [Y or N]")

    @Decorators.decorator_write_log_init_end_method
    def question_symbol_obstacles(self) -> str:
        while True:
            agree_obstacles_symbol = input("Obstacles are represents with '#', are you agree [Y, N]: \n")
            if agree_obstacles_symbol == "Y":
                return "#"
            elif agree_obstacles_symbol == "N":
                base_element_obstacle = input("Please enter corridor symbol to use in labyrinth: \n")
                return base_element_obstacle
            else:
                self.logger.warning(f"[question symbol obstacles] incorrect question option, "
                                    f"input : {agree_obstacles_symbol}")
                print("Incorrect option, please enter [Y or N]")

    @Decorators.decorator_write_log_init_end_method
    def initial_question_user_method_input_labyrinth(self) -> int:
        while True:
            option_chosen = input("\n\nInit labyrinth (select an option):"
                                  "\n- 1. from file \n- 2. directly here"
                                  "\n- 3. automatic generation\n\nChosen option:\n")
            msg_error = "\n\nIncorrect option, please enter only numeric values, [1, 2 or 3, amongst options]"
            try:
                option_chosen_int = int(option_chosen)
                if option_chosen_int in [1, 2, 3]:
                    return option_chosen_int
                else:
                    print(msg_error)
            except ValueError as err:
                self.logger.warning(f"[initial question user method input labyrinth] incorrect question option, "
                                    f"error : {err}")
                print(msg_error)

    @Decorators.decorator_write_log_init_end_method
    def question_file_name(self) -> str:
        while True:
            file_name = input("\n\nIndicate file name [file has to be in 'input' folder, txt format, see example,"
                              "'example_labyrinth.txt': \n")
            msg_error = "\n\nFile not found, indicate properly file name in input folder with txt format"
            try:
                file_name_searched_in_input_folder = [file for file in os.listdir("input/")
                                                      if file_name in file and ".txt" in file][0]
                return file_name_searched_in_input_folder
            except IndexError as err:
                self.logger.warning(
                    f"[question file name] not found file, "
                    f"error : {err}")
                print(msg_error)

    @Decorators.decorator_write_log_init_end_method
    def question_symbols_on_file_or_list(self,
                                         format_input) -> tuple:
        symbol_space = input(f"\n\nIndicate space corridors symbol in your {format_input}"
                             " [for example, in example file 0 it´s space-corridors]: \n")

        symbol_obstacle = input(f"\n\nIndicate obstacle symbol in your {format_input}"
                                " [for example, in example file 1 it´s wall-obstacle]: \n")

        return symbol_space, symbol_obstacle

    @Decorators.decorator_write_log_init_end_method
    def question_direct_list(self) -> list:
        while True:
            matrix = input("\n\nIndicate direct list [see example,"
                           "[[0, 1, 0],[1, 0, 0]]: \n")
            msg_error = "\n\nlist not properly indicated [see example, " \
                        "[[0, 1, 0],[1, 0, 0]]: \n"
            try:
                dimension_y = matrix.count("[") - 1
                dimension_x = len(
                    [element.replace("]", "") for element in matrix.split("[") if len(element) >= 1][0].split(",")) - 1

                matrix = [element.split(",") for element in [element.replace("]", "") for element in matrix.split("[")
                                                             if len(element) >= 1] if element.split(",") != '  ']
                base_matrix_labyrinth = []
                for element_in_y_dimension in range(dimension_y):
                    row = []
                    for element_in_x_dimension in range(dimension_x):
                        row.append(str(matrix[element_in_y_dimension][element_in_x_dimension].replace("'", "").strip()))
                    base_matrix_labyrinth.append(row)
                return base_matrix_labyrinth
            except Exception as err:
                self.logger.warning(
                    f"[question direct list] not properly indicated list, "
                    f"error : {err}")
                print(msg_error)
