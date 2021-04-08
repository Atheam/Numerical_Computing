import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt 


def integrate_trapz(x,y):
    n = len(x)
    sum = 0

    for i in range(n-1):
        h = (x[i+1]-x[i])
        sum+= (y[i]+y[i+1])*h/2

    return sum


lib_vals = []
f_vals = []

for points in range(50,1000,5):
    x_v = list(np.linspace(1,500,points))
    y_v = [x**5*np.exp(-x)*np.sin(x) for x in x_v]

    f_vals.append(integrate_trapz(x_v,y_v))
    lib_vals.append(integrate.trapz(y_v,x_v))


plt.plot(range(50,1000,5),f_vals,"r")
plt.plot(range(50,1000,5),lib_vals,"b")
plt.show()


    




