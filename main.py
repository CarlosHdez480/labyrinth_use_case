from src.Logger import Logger
from src.InputMatrixLabyrinthData import InputMatrixLabyrinthData

logger_object = Logger("log_labyrinth_solver")
logger = logger_object.create_logger_file("Solver Labyrinth")

labyrinth_matrix, symbol_space, symbol_obstacle = InputMatrixLabyrinthData().get_matrix_asking_user()

print(labyrinth_matrix)
print("symbol space: " + symbol_space)
print("symbol obstacle: " + symbol_obstacle)
