''' You can change the value of grid and replace them with the value of your own sudoku '''
''' Sudoku are taken from website : https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html'''

grid=[[1,0,0,4,8,9,0,0,6],
      [7,3,0,0,0,0,0,4,0],
      [0,0,0,0,0,1,2,9,5],
      [0,0,7,1,2,0,6,0,0],
      [5,0,0,7,0,3,0,0,8],
      [0,0,6,0,9,5,7,0,0],
      [9,1,4,6,0,0,0,0,0],
      [0,2,0,0,0,0,0,3,7],
      [8,0,0,5,1,2,0,0,4]]

'''

Author Name: Manas Gupta
Date Modified: 10:42 PM  2/14/2020
Description : Sodoku Solver using backtracking and recursion

'''


def test(y,x,num):
    global grid
    for i in range (0,9):                   # to check in the same column 
        if grid[y][i] ==num :
            return False   
        
    for i in range (0,9) :                  #  to check in the same row  
        if grid[i][x] ==num :
            return False
    
    
    x_box=(x//3)*3
    y_box=(y//3)*3
    
    for i in range (0,3):                   #  to check in a specific block 
        for j in range (0,3):
            if grid[y_box+i][x_box+j]==num:
                return False
            
    return True     

import numpy as np
'''
This code using backtracking and recursion this will hit and try and when it gets that its not the 
best fitting case then it runs again from the start 
'''
def solveMatrix() :
    global grid
    for y in range (9) :
        for x in range (9):
            if grid[y][x] == 0 :
                for num in range (1,10):                
                    if test(y,x,num) :
                        grid[y][x]=num
                        solveMatrix()
                        grid[y][x]=0
                        
                return
            
    print(np.matrix(grid))
                    

solveMatrix()                    