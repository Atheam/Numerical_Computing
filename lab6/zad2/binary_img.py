import numpy as np
from copy import copy


def cost(img,energy_func):
    cost = 0
    n = img.shape[0]
    for row in range(n):
        for col in range(n):
            if img[row][col] == 1:
                cost+= energy_func(img,row,col)
    return cost

def swap(img):
    swapped = copy(img)
    n = img.shape[0]
    a,b = np.random.randint(0,n,(2,1))
    c,d = np.random.randint(0,n,(2,1))
    while swapped[a,b] == swapped[c,d] or (a,b) == (c,d):
        a,b = np.random.randint(0,n,(2,1))
        c,d = np.random.randint(0,n,(2,1))
    swapped[a,b], swapped[c,d] = swapped[c,d], swapped[a,b]
    return swapped

def cool(T,rate):
    return T *rate

def annealing(img,T,max_iter,rate,energy_func):
    T_init = T
    temp = [T]
    costs = [cost(img,energy_func)]
    for i in range(max_iter):
        new_img = swap(img)

        old_cost = cost(img,energy_func)
        new_cost = cost(new_img,energy_func)

        if new_cost <= old_cost:
            img = new_img
            costs.append(new_cost)
        else:
            if np.random.uniform(0,1) < np.exp((old_cost - new_cost)/T): 
                img = new_img
                costs.append(new_cost)
            else:
                costs.append(old_cost)

        T = cool(T,rate)
        temp.append(T)
        
        if i % (max_iter*0.15) == 0:
            T_init *= 0.8
            T += T_init

    return img,costs,temp







