import numpy as np
from copy import copy
import matplotlib.pyplot as plt


def cost(sudoku):
    cost = 0
    for row in sudoku:
        cost += len(row) - len(set(row))
    for col in sudoku.T:
        cost += len(col) - len(set(col))
    
    for i in range(0,7,3):
        for j in range(0,7,3):
            square = sudoku[i:i+3,j:j+3].reshape(9,)
            cost += len(square) - len(set(square))

    return cost

def swap(sudoku,sudoku_info):
    swapped = copy(sudoku)
    n = swapped.shape[0]
    a = np.random.randint(0,n)
    b = np.random.randint(0,n)
    c = np.random.randint(0,n)

    while b == c or sudoku_info[a,b] or sudoku_info[a,c]:
            a = np.random.randint(0,n)
            b = np.random.randint(0,n)
            c = np.random.randint(0,n)
        
    swapped[a,b], swapped[a,c] = swapped[a,c], swapped[a,b]

    return swapped 

def cool(T,rate):
    return T*rate   

def annealing(sudoku,sudoku_info,T,max_iter,rate):
    T_init = T
    temp = [T]
    costs = [cost(sudoku)]
    for i in range(max_iter):
        new_sudoku = swap(sudoku,sudoku_info)

        old_cost = cost(sudoku)
        new_cost = cost(new_sudoku)
        if new_cost == 0:
            return sudoku,costs,temp
            
        if new_cost <= old_cost:
            sudoku = new_sudoku
            costs.append(new_cost)
        else:
            if np.random.uniform(0,1) < np.exp((old_cost - new_cost)/T): 
                sudoku = new_sudoku
                costs.append(new_cost)
            else:
                costs.append(old_cost)
        T = cool(T,rate)
        temp.append(T)
        
        if i % (max_iter*0.1) == 0:
            T_init = T_init*0.9
            T = T_init


    return sudoku,costs,temp







