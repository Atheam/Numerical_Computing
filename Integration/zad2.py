import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt 


def integrate_simpson(x,y):
    n = len(x)
    h = x[2] - x[0]
    sum = 0
    for i in range(0,n-2,2):
        sum+= y[i] + 4*y[i+1] + y[i+2]
    sum*=h
    return sum/6


lib_vals = []
f_vals = []

for points in range(50,500,5):
    x_v = list(np.linspace(1,500,points))
    y_v = [x**5*np.exp(-x)*np.sin(x) for x in x_v]

    f_vals.append(integrate_simpson(x_v,y_v))
    lib_vals.append(integrate.simps(y_v,x_v))
    

plt.plot(range(50,500,5),f_vals, "r")
plt.plot(range(50,500,5),lib_vals,"b")
plt.show()

