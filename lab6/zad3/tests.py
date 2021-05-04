import matplotlib.pyplot as plt
import numpy as np
from sudoku import annealing,cost

def read_file(filename):
    out = []
    with open(filename,"r") as f:
        txt = f.readlines()
        for line in txt:
            out_line = []
            for char in line:
                if char == ' ' or char == '\n':
                    continue
                if char == 'x':
                    out_line.append(0)
                else:
                    out_line.append(char)
            out.append(out_line)

    
    out = [list(map(int,i)) for i in out]
    sudoku_info = [[True if x != 0 else False for x in row] for row in out]
    
    return np.array(out),np.array(sudoku_info)

def fill_sudoku(sudoku):
    n = sudoku.shape[0]
    for i in range(n):
        for j in range(n):
            if sudoku[i][j] == 0:
                sudoku[i][j] = list((set(range(1,10)) - set(sudoku[i])))[0]
    return sudoku

def test_sudoku(filename,T,max_iter,rate):

    init_sudoku,sudoku_info = read_file(filename)
    init_sudoku = fill_sudoku(init_sudoku)
    
    print(init_sudoku)
    after_sudoku,costs,temp = annealing(init_sudoku, sudoku_info, T, max_iter, rate)
    print(after_sudoku)
    print(cost(after_sudoku))
    fig,ax = plt.subplots(2)
    ax[0].plot(costs)
    ax[0].set_title("Cost")
    ax[1].plot(temp)
    ax[1].set_title("Temperature")
    plt.tight_layout()
    plt.show()



test_sudoku("sudoku.txt", 1, 1000000, 0.999)

