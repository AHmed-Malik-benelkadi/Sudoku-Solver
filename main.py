from brute_force_solver import BruteForceSolver
from backtracking_solver import BacktrackingSolver
from display import display_sudoku
import time

def read_sudoku_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        grid = []
        for line in lines:
            grid.append([int(cell) if cell != "_" else 0 for cell in line.strip()])
        return grid

initial_grid = read_sudoku_from_file("sudoku.txt")
solver_grid = [row.copy() for row in initial_grid]

# Use the solver (BacktrackingSolver)
solver = BacktrackingSolver(solver_grid)

# Solve the Sudoku
start_time = time.time()
solver.solve()
end_time = time.time()

print(f"Time taken: {end_time - start_time} seconds\n")

# Display the result using Pygame
display_sudoku(initial_grid, solver.grid)
