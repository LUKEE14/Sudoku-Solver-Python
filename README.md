# Sudoku Solver-Python
 Developing a sudoku solver using Backtracking algorithm in python


 grid = [
[4,0,0,0,0,5,0,0,0],
[0,0,0,0,0,0,1,9,8],
[3,0,0,0,8,2,4,0,0],
[0,0,0,1,0,0,0,8,0],
[9,0,3,0,0,0,0,0,0],
[0,0,0,0,3,0,6,7,0],
[0,5,0,0,0,9,0,0,0],
[0,0,0,2,0,0,9,0,7],
[6,4,0,3,0,0,0,0,0]]

import pyautogui as pg
import numpy as np
import time

grid = []

while True:
    row = list(input("Row:"))
    ints= []

    for n in row:
        ints.append(int(n))
    grid.append(ints)

    if len(grid) == 9:
        break
    print('row' + str(len(grid)) + 'complete')


time.sleep(1)


def attainable(x,y,n):
    #checks Rows
    for i in range(0,9):  
        if grid[i][x] == n and i != y:
            return False

    #checks Columns    
    for i in range(0,9):
        if grid[y][i] == n and i != x:
            return False
        
    #checks for numbers in the box , no matter the position   
    x0 = (x // 3) * 3
    y0 = (x // 3) * 3
    for x in range (x0, x0 + 3):
        for v in range(y0, y0 + 3):
            if grid[y][x] == n:
                return False
            
    return True

def Print(matrix):
    final = []
    str_fin = []
    for i in range(9):
        final.append(matrix[i])

    for lists in final:
        for num in lists:
            str_fin.append(str(num))

    counter = []

    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter)%9 == 0:
            pg.hotkey('down')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left') 
            
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if attainable(x,y,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(grid)
    input("More ?")

solve()