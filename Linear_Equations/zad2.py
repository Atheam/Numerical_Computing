import numpy as np
from copy import deepcopy

def LU_factorization(A):
    n = A.shape[0]

    for col in range(n):
        for row in range(col+1,n):
            multiplier = A[row][col] / A[col][col]
            A[row][col+1:n] -= multiplier * A[col][col+1:n]
            A[row][col] = multiplier

    return A 


def generate_matrix(n):
	A = np.random.uniform(0,n,(n,n))
	return A


A = generate_matrix(50)
A_copy = deepcopy(A)


result = LU_factorization(A_copy)
U = np.triu(result)
L = np.tril(result)
np.fill_diagonal(L,1)

print(abs(A - L@U) < 0.0000000001)

