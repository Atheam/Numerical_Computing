from TSP import annealing,arbitrary_swap,consecutive_swap,cost
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from random import choice


def test_TSP(n,T,max_iter,rate,distribution,swap,animate = False):
    if distribution == "uniform":
        init_path = np.random.uniform(0,1,(n,2))

    if distribution == "normal":
        init_path = np.random.normal(0,1,(n,2))

    if distribution == "groups":
        init_path = np.random.uniform(0,1,(n,2))
        for i in range(n):
            init_path[i][0] = init_path[i][0]*0.1 + choice([0,0.45,0.9])
            init_path[i][1] = init_path[i][1]*0.1 + choice([0,0.45,0.9])

    if animate:
        after_path,temp,costs,paths = annealing(init_path,T,max_iter,rate,swap,animate = True)
    else:
        after_path,temp,costs = annealing(init_path,T,max_iter,rate,swap)
    print(cost(after_path))

    if animate:
        fig,ax = plt.subplots()
        def draw(i):
            ax.clear()
            ax.plot(paths[i][:,0],paths[i][:,1])

        animated = animation.FuncAnimation(fig, draw,interval = 100,frames = n)
        plt.show()
    
    init_path = np.concatenate((init_path,init_path[0].reshape(1,2)))
    after_path = np.concatenate((after_path,after_path[0].reshape(1,2)))


    fig,ax = plt.subplots(2,2)

    ax[0,0].plot(init_path[:,0],init_path[:,1])
    ax[0,0].set_title("Initial path")
    ax[0,1].plot(after_path[:,0],after_path[:,1])
    ax[0,1].set_title("Path after annealing")
    ax[1,0].plot(temp)
    ax[1,0].set_title("Temperature")
    ax[1,1].plot(costs)
    ax[1,1].set_title("Cost")
    plt.tight_layout()
    plt.show()


test_TSP(n = 30, T = 1, max_iter = 40000, rate = 0.9995, distribution = "uniform", swap = arbitrary_swap)




