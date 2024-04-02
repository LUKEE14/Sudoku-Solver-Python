import pyautogui as pg 
import numpy as np
import time

grid = []

while True:
    row = list(input('Row: '))
    ints = []

    for n in row:
        ints.append(int(n))
    grid.append(ints)

    if len(grid) == 9:
        break
    print('Row ' + str(len(grid)) + ' Complete')

time.sleep(1)

def is_attainable(x, y, n):
    global grid

    # Checks for number (n) in row and column
    for i in range(0, 9):
        if (grid[y][i] == n) or (grid[i][x] == n):
            return False

    # Checks for number (n) in 3x3 grid
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True

def find_empty_location():
    global grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None, None

def solve():
    global grid
    row, col = find_empty_location()
    if row is None and col is None:
        return True

    for num in range(1, 10):
        if is_attainable(col, row, num):
            grid[row][col] = num
            if solve():
                return True
            grid[row][col] = 0
    return False

def print_grid():
    global grid
    for row in grid:
        for num in row:
            pg.press(str(num))
            pg.hotkey('right')
        pg.hotkey('down')
        pg.hotkey('left' * 8)

if solve():
    print_grid()
    input("More?")


        