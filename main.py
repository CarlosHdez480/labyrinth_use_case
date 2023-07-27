"""main script to solve maze"""
from src.logger import Logger
from src.input_matrix_labyrinth_data import InputMatrixLabyrinthData
from src.solver import MazeSolver

# set log file
logger_object = Logger("log_labyrinth_solver")
logger = logger_object.create_logger_file("Solver Labyrinth")

# create object
solver_object = MazeSolver(logger)
input_labyrinth_object = InputMatrixLabyrinthData()

# create labyrinth
labyrinth_matrix, symbol_space, symbol_obstacle = input_labyrinth_object.get_matrix_asking_user()

# solver
print("\n\n####### MATRIX #######")
print("matrix: \n")
print(labyrinth_matrix)
print("\nsymbol space: " + symbol_space)
print("symbol obstacle: " + symbol_obstacle)

print("\n\n####### RESULT #######")
MIN_MOVEMENTS_TO_SOLVE_MAZE = solver_object.find_min_movements(labyrinth_matrix,
                                                               symbol_space,
                                                               symbol_obstacle)
print(f"\n\nRESULT: min movements [-1, it´s impossible]: {MIN_MOVEMENTS_TO_SOLVE_MAZE}")
