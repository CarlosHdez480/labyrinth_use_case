from src.GenerateLabyrinth import GenerateLabyrinth
from src.Logger import Logger

logger_object = Logger("log_labyrinth_solver")
logger = logger_object.create_logger_file("Solver Labyrinth")

option_chosen = input("Init labyrinth (select an option):"
                      "\n- 1. from file \n- 2. directly here"
                      "\n- 3. automatic generation\n\nChosen option:")

if option_chosen == "3":
    while True:
        dimensions_matrix = input("Indicate labyrinth dimensions labyrinth (x, y): \n")
        msg_dimensions_error = "Incorrect dimensions, please enter values properly [numeric values" \
                               " separated by comma, for instance [5, 6]"
        try:
            dimensions_matrix_x = dimensions_matrix.split(",")[0].replace("[",
                                                                          "").strip()
            dimensions_matrix_y = dimensions_matrix.split(",")[1].replace("]",
                                                                          "").strip()
            try:
                dimensions_matrix_x = int(dimensions_matrix_x)
                dimensions_matrix_y = int(dimensions_matrix_y)
                break
            except ValueError as err:
                logger.warning(f"[main] not numeric value, value error: {err}")
                print("Not numeric value. " + msg_dimensions_error)
            except ValueError as err:
                logger.warning(f"[main] not numeric value, value error: {err}")
                print("Not numeric value. " + msg_dimensions_error)
        except IndexError as err:
            logger.warning(f"[main] not indicated dimensions properly, index error: {err}")

    while True:
        probability_find_obstacle_input = input("Indicate probability find obstacle [value amongst 0 - 1]: \n")
        msg_probability_error = "Incorrect probability, value error, please enter values properly [value amongst 0 - 1]"
        try:
            probability_find_obstacle = float(probability_find_obstacle_input)
            if (probability_find_obstacle > 0) & (probability_find_obstacle < 1):
                break
            else:
                print(msg_probability_error)
        except ValueError as err:
            logger.warning(f"[main] not indicated probability properly, value error: {err}")
            print(msg_probability_error)

    while True:
        agree_corridors_symbol = input("Corridors are represents with '.', are you agree [Y, N]: \n")
        if agree_corridors_symbol == "Y":
            base_element_not_obstacle = "."
            break
        elif agree_corridors_symbol == "N":
            base_element_not_obstacle = input("Please enter corridor symbol to use in labyrinth: \n")
            break
        else:
            print("Incorrect option, please enter [Y or N]")

    while True:
        agree_obstacles_symbol = input("Obstacles are represents with '#', are you agree [Y, N]: \n")
        if agree_obstacles_symbol == "Y":
            base_element_obstacle = "#"
            break
        elif agree_obstacles_symbol == "N":
            base_element_obstacle = input("Please enter corridor symbol to use in labyrinth: \n")
            break
        else:
            print("Incorrect option, please enter [Y or N]")

    object_generator_labyrinth = GenerateLabyrinth()
    labyrinth_matrix = object_generator_labyrinth.create_labyrinth([dimensions_matrix_x, dimensions_matrix_y],
                                                                   base_element_not_obstacle,
                                                                   base_element_obstacle,
                                                                   probability_find_obstacle,
                                                                   )

    print(labyrinth_matrix)