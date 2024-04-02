# Sudoku Solver

This Python program is designed to solve Sudoku puzzles efficiently using the backtracking algorithm.

## Requirements

Python 3.x
PyAutoGUI library

## Installation

Clone this repository to your local machine.
Install the required Python libraries using pip:

pip install pyautogui

## Running the Solver

Input the Sudoku puzzle row-wise, with each row entered on a separate line. Use '0' to represent empty cells.
Once the puzzle is entered, the solver will automatically start solving it.
After solving, the program will display the solved Sudoku puzzle using PyAutoGUI.
Press Enter to continue and solve more Sudoku puzzles if desired.

## How it Works

The Sudoku solver employs the backtracking algorithm to efficiently find the solution to a given puzzle. Here's how it works:

The program takes input from the user, representing the Sudoku puzzle as a 9x9 grid. Empty cells are represented by '0'.
The solver uses a recursive backtracking approach to fill in the empty cells of the grid. It systematically tries different numbers in each cell and backtracks when it encounters a conflict (i.e., a number cannot be placed in a certain position).
To improve efficiency, the solver uses constraint propagation techniques such as checking for attainability in rows, columns, and 3x3 subgrids. It also employs techniques like Naked Singles and Hidden Singles to reduce the search space and speed up the solving process.

Once a solution is found, the solver displays the solved Sudoku puzzle using PyAutoGUI for visualization.
