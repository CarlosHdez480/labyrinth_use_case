from src.Decorators import Decorators
from src.Logger import Logger
from src.ReadData import ReadData
from src.QuestionsUsers import QuestionsUsers
from src.GenerateLabyrinth import GenerateLabyrinth


class InputMatrixLabyrinthData:
    """
        A class to read input data given by user to create initial labyrinth.

        ...

        Attributes
        ----------
            - logger (logging): The log file.

        Methods
        -------
            - get_matrix_asking_user(): ask user by way to input labyrint data.
        """

    def __init__(self,
                 logger=None):
        """
        Constructs a InputData object.

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
        self.object_questions = QuestionsUsers(self.logger)

    @Decorators.decorator_write_log_init_end_method
    def get_matrix_asking_user(self):
        """
        Create base labyrinth matrix asking user ways to input data, labyrinth itself.

        ...

        Parameters
        ----------
            :return: matrix with labyrinth created from source indicated by user.
            :rtype: list
        """
        option_user_select = self.__input_option_question()
        matrix, symbol_space, symbol_obstacle = self.__evaluate_option_selection_operator_input_and_return_matrix(option_user_select)
        return matrix, symbol_space, symbol_obstacle

    @Decorators.decorator_write_log_init_end_method
    def __input_option_question(self):
        option_chosen = self.object_questions.initial_question_user_method_input_labyrinth()
        return option_chosen

    @Decorators.decorator_write_log_init_end_method
    def __evaluate_option_selection_operator_input_and_return_matrix(self,
                                                                     option_selected: str):
        if option_selected == 1:
            base_labyrinth, symbol_space, symbol_obstacle = self.__option_selected_first_from_file()
            return base_labyrinth, symbol_space, symbol_obstacle
        elif option_selected == 2:
            base_labyrinth = self.__option_selected_second_from_direct_list()
            return base_labyrinth
        elif option_selected == 3:
            base_labyrinth, symbol_space, symbol_obstacle = self.__option_selected_third_created_inside()
            return base_labyrinth, symbol_space, symbol_obstacle
        else:
            self.logger.error("matrix not generation possible, it failed entry options")
            return [[]]

    @Decorators.decorator_write_log_init_end_method
    def __option_selected_third_created_inside(self):
        object_generator_labyrinth = GenerateLabyrinth(self.logger)

        dimensions = self.object_questions.question_matrix_dimensions()
        probability = self.object_questions.question_probability_obstacles()

        symbol_corridors = self.object_questions.question_symbol_corridors()
        symbol_obstacles = self.object_questions.question_symbol_obstacles()

        labyrinth_matrix = object_generator_labyrinth.create_labyrinth(dimensions,
                                                                       symbol_corridors,
                                                                       symbol_obstacles,
                                                                       probability,
                                                                       )
        return labyrinth_matrix, symbol_corridors, symbol_obstacles

    @Decorators.decorator_write_log_init_end_method
    def __option_selected_first_from_file(self):
        object_reader = ReadData(self.logger)

        file = self.object_questions.question_file_name()
        labyrinth_matrix = object_reader.read_txt_file(file)

        if not labyrinth_matrix:
            raise Exception("error reading file, please enter file in input folder in txt format and with format of "
                            "example_labyrinth.txt")
        else:
            space_symbol, obstacle_symbol = self.object_questions.question_symbols_on_file()
            return labyrinth_matrix, space_symbol, obstacle_symbol

    @Decorators.decorator_write_log_init_end_method
    def __option_selected_second_from_direct_list(self):
        file = self.object_questions.question_file_name()
        pass
