import numpy as np
import time
from copy import deepcopy

def gauss_jordan(A:np.array,B:np.array) -> np.array:
	n = A.shape[0]

	for col in range(n):

		pivot_idx = np.argmax(np.abs(A[:,col][col:])) + col
		A[[col,pivot_idx]] = A[[pivot_idx,col]]
		B[col],B[pivot_idx] = B[pivot_idx],B[col]
	
		for row in range(n):
			if row == col:
				continue
			multiplier = A[row,col]/A[col,col]	
			
			A[row] -= multiplier * A[col]
			B[row] -= multiplier * B[col]

	return B/np.diag(A)


def generate_matrix(n):
	A = np.random.uniform(0,n,(n,n))
	B = np.random.uniform(0,n,(n,))
	return A,B


A1,B1 = generate_matrix(500)
A2,B2 = generate_matrix(600)
A3,B3 = generate_matrix(700)
A4,B4 = generate_matrix(800)
A5,B5 = generate_matrix(900)
A6,B6 = generate_matrix(1000)
A7,B7 = generate_matrix(1100)
A8,B8 = generate_matrix(1200)
A9,B9 = generate_matrix(1300)
A10,B10 = generate_matrix(1400)


tab = [(A1,B1),(A2,B2),(A3,B3),(A4,B4),(A5,B5),(A6,B6),(A7,B7),(A8,B8),(A9,B9),(A10,B10)]
GJ_res = []
LS_res =[]
LL_res = []

for count,pair in enumerate(tab,start= 5): 
	A_copy1= deepcopy(pair[0])
	B_copy1= deepcopy(pair[1])
	A_copy2= deepcopy(pair[0])
	B_copy2= deepcopy(pair[1])
	A_copy3= deepcopy(pair[0])
	B_copy3= deepcopy(pair[1])
	
	start = time.time()
	gauss_jordan(A_copy1,B_copy1)
	end = time.time()
	print(count*100," Gauss-Jordan: ",end-start)
	GJ_res.append((count*100,end-start))

	start = time.time()
	np.linalg.solve(A_copy2,B_copy2)
	end = time.time()
	print(count*100," linalg.solve: ",end-start)
	LS_res.append((count*100,end-start))

	start = time.time()
	np.linalg.lstsq(A_copy3,B_copy3)
	end = time.time()
	print(count*100," linalg.lstsq: ",end-start)
	LL_res.append((count*100,end-start))


import matplotlib.pyplot as plt

plt.scatter(*zip(*GJ_res),label = "gauss_jordan time")
plt.scatter(*zip(*LS_res),label = "linalg.solve time")
plt.scatter(*zip(*LL_res),label = "linalg.lstq time")
plt.title("Algorthims times solving n by n equation")
plt.ylabel("seconds")
plt.xlabel("n dimensions")
plt.legend()
plt.show()




