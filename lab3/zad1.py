import numpy as np
from matplotlib import pyplot as plt
from math import factorial

interval = (-5, 5)
N = [5,10,15]


def f(x):
    return 1/(1 + x**2)

def forwardDiff(k, f, nodes, i):
    if k == 0:
        return f(nodes[i])
    return forwardDiff(k-1, f, nodes, i+1) - forwardDiff(k-1, f, nodes, i)

def binomial_coeff(n, k):
    product = 1
    for i in range(k):
        product*= n - i
    return product/factorial(k)

def interpolate(nodes, N, x, f, forwardDiff):
    out = 0
    s = (x-nodes[0])/(nodes[1]-nodes[0])
    for k in range(N + 1):
        out += binomial_coeff(s, k)*forwardDiff[k]
    return out


for n in N: 
    nodes = np.linspace(interval[0], interval[1],n+1)
    forwardDiffs = [forwardDiff(k,f,nodes,0) for k in range(n+1)]

    x = np.linspace(interval[0], interval[1],10000)
    
    interpolation = [interpolate(nodes,n,x[i],f,forwardDiffs) for i in range(10000)]
    y = [f(x[i]) for i in range(10000)]

    err_x = np.linspace(interval[0],interval[1],30)
    err = [abs(interpolate(nodes,n,err_x[i],f,forwardDiffs) - f(err_x[i])) for i in range(30)]

    plt.plot(x, interpolation,"blue")
    plt.plot(x, y,"yellow")
    #plt.plot(err_x, err,"r")
    plt.show()