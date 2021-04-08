from scipy import integrate
from math import sqrt
import matplotlib.pyplot as plt 

f4 = lambda y,x: 1/((sqrt(x+y)*(1+x+y)))

f5 = lambda y,x: x**2 + y**2

def integrate_2D(f,x_a,x_b,y_a,y_b,x_n = 100,y_n = 100):
    sum = 0
    hx = (x_b - x_a)/(x_n-1)
    
    x = 0
    for _ in range(0,x_n-1):
        y = 0
        hy = (y_b(x) - y_a(x))/(y_n-1)
        integral = 0

        for _ in range(0,y_n-1):
            integral += (f(y,x) + f(y+hy,x))*hy/2
            y += hy
    
        sum+=integral
        x += hx

    return sum/y_n



f_vals = []

for points in range(5,50,1):
  
    f_vals.append(integrate_2D(f5,0,1,lambda x: 0,lambda x: 1-x,points,points))
    

lib_vals = [integrate.dblquad(f5,0,1,lambda x: 0,lambda x: 1-x)[0] for _ in range(5,50,1)]
plt.plot(range(5,50,1),f_vals, "r")
plt.plot(range(5,50,1),lib_vals,"b")
plt.show()




        







