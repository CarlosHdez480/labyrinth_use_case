"""main script to solve maze"""
from src.logger import Logger
from src.input_matrix_labyrinth_data import InputMatrixLabyrinthData
from src.solver import MazeSolver

logger_object = Logger("log_labyrinth_solver")
logger = logger_object.create_logger_file("Solver Labyrinth")

solver_object = MazeSolver(logger)
input_labyrinth_object = InputMatrixLabyrinthData()

labyrinth_matrix, symbol_space, symbol_obstacle = input_labyrinth_object.get_matrix_asking_user()

print("matrix: \n")
print(labyrinth_matrix)
print("symbol space: " + symbol_space)
print("symbol obstacle: " + symbol_obstacle)

min_moment_to_solve_maze = solver_object.find_min_movements(labyrinth_matrix,
                                                            symbol_space,
                                                            symbol_obstacle)
print(f"\n\nRESULT: min movements [-1, it´s impossible]: {min_moment_to_solve_maze}")
