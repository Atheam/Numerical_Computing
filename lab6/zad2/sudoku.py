import numpy as np
import collections

table = np.empty((9,9),int)

filename = "sudoku.txt"
with open(filename,"r") as f:
    text = f.read().split("\n")
    text = text[:-1]
    for row,line in enumerate(text):
        chars = line.split(" ")
        print(chars)
        for col in range(len(chars)):
            table[row][col] = chars[col]
print(table)









        


