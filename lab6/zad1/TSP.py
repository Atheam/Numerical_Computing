import numpy as np
from math import sqrt
from copy import copy

def dist(a,b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    
def cost(path):
    n = len(path)
    return np.sum([dist(path[i],path[i+1]) for i in range(n-1)]) + dist(path[0],path[n-1])

def arbitrary_swap(path):
    swapped = copy(path)
    n = len(path)

    a = np.random.randint(0,n-1)
    b = np.random.randint(0,n-1)
    while a == b:
        a = np.random.randint(0,n-1)
        b = np.random.randint(0,n-1)

    swapped[[a,b]] = swapped[[b,a]] 
    return swapped

def consecutive_swap(path):
    swapped = copy(path)
    n = len(path)
    a = np.random.randint(0,n-2)
    swapped[[a,a+1]] = swapped[[a+1,a]]
    return swapped

def cool(T,rate):
    return T * rate


def annealing(path,T,max_iter,rate,swap,animate = False):
    temp = [T]
    T_init = T

    costs = [cost(path)]
    if animate:
        paths = []
    for i in range(max_iter):
        new_path = swap(path)

        old_cost = cost(path)
        new_cost = cost(new_path)

        if new_cost <= old_cost:
            path = new_path
            costs.append(new_cost)
        else:
            if np.random.uniform(0,1) < np.exp((old_cost - new_cost)/T): 
                path = new_path
                costs.append(new_cost)
            else:
                costs.append(old_cost)
                
        T = cool(T,rate)

        # if i%(max_iter*0.3) == 0:
        #      T_init *=0.7
        #      T = T_init

        temp.append(T)
        if animate:
            paths.append(path)

    if animate:
        return path,temp,costs,paths
    else:
        return path,temp,costs

