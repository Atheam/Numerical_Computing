import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from copy import deepcopy

def dist(a,b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    
def cost(path):
    cost = 0
    n = len(path)
    for i in range(n):
        cost += dist(path[i % n],path[(i+1) % n]) 
    return cost


def swap(path):
    swapped = deepcopy(path)
    n = len(path)

    a = np.random.randint(0,n-1)
    b = np.random.randint(0,n-1)
    while a == b:
        a = np.random.randint(0,n-1)
        b = np.random.randint(0,n-1)

    swapped[[a,b]] = swapped[[b,a]] 
    return swapped


def cool(T,rate):
    return T * rate

def annealing(path):
    T = 1000
    temp = [T]
    for _ in range(1000000):
        prev_cost = cost(path)
        swapped = swap(path)
        if cost(swapped) <= cost(path):
            path = swapped
        else:
            if np.random.uniform(0,1) < np.exp((cost(path) - cost(swapped))/T):
                path = swapped
        T = cool(T,0.99995)
        temp.append(T)

    return path,temp

n = 100

path = np.random.uniform(0,1,(n,2))


print(cost(path))
path,temp = annealing(path)
print(cost(path))



plt.plot(path[:,0],path[:,1])
plt.show()
plt.plot(temp)
plt.show()








