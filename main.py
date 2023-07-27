from src.Logger import Logger
from src.InputMatrixLabyrinthData import InputMatrixLabyrinthData


logger_object = Logger("log_labyrinth_solver")
logger = logger_object.create_logger_file("Solver Labyrinth")

labyrinth_matrix = InputMatrixLabyrinthData().get_matrix_asking_user()

print(labyrinth_matrix)