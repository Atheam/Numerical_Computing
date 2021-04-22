from zad1 import bisection_method
from zad2 import newton_method
from zad3 import sectant_method
import mpmath as mp
import math
import matplotlib.pyplot as plt
import numpy as np

f1 = lambda x : mp.cos(x)*mp.cosh(x) - 1
f1_derivative = lambda x: mp.cos(x) * mp.sinh(x) - mp.sin(x) * math.cosh(x)
f2 = lambda x : float("inf") if x == 0 else 1/x -mp.tan(x)
f2_derivative = lambda x: float("inf") if x == 0 else (-1/x**2) - (1/mp.cos(x)**2)
f3 = lambda x : 2**-x + mp.exp(x) + 2*mp.cos(x) - 6
f3_derivative = lambda x: mp.exp(x) - 2**-x * mp.log(math.e,2) - mp.sin(x)

epsilons = [1e-7,1e-15,1e-33]
print("\n\n---------------RESULTS FOR BISECTION METHOD ---------------------\n\n")
print("RESULTS FOR FIRST FUNCTION")
for eps in epsilons:
    try:
        root, i = bisection_method(f1, 1.5*math.pi, 2*math.pi, 64,eps)
        print("Root:", root,"Iterations:",i,"Epsilon:",eps)
    except Exception as err:
        print(repr(err))

print("RESULTS FOR SECOND FUNCTION")
for eps in epsilons:
    try:
        root, i = bisection_method(f2, 0, 0.5*math.pi, 64,eps)
        print("Root:", root,"Iterations:",i,"Epsilon:",eps)
    except Exception as err:
        print(repr(err))

print("RESULTS FOR THIRD FUNCTION")
for eps in epsilons:
    try:
        root, i = bisection_method(f3, 1, 3, 64,eps)
        print("Root:", root,"Iterations:",i,"Epsilon:",eps)
    except Exception as err:
        print(repr(err))

print("\n\n------------------RESULTS FOR NEWTON METHOD-----------------------\n\n")
print("RESULTS FOR FIRST FUNCTION")
for eps in epsilons:
    try:
        root,i = newton_method(f1, f1_derivative, 1.5*math.pi, 2*math.pi, 64,eps, 100)
        print("Root:", root,"Iterations:",i,"Epsilon:",eps)
    except Exception as err:
        print(repr(err))
    
print("RESULTS FOR SECOND FUNCTION")
for eps in epsilons:
    try:
        root,i = newton_method(f2, f2_derivative, 0, 0.5*math.pi, 64,eps, 100)
        print("Root:", root,"Iterations:",i,"Epsilon:",eps)
    except Exception as err:
        print(repr(err))
    
print("RESULTS FOR THIRD FUNCTION")
for eps in epsilons:
    try:
        root,i = newton_method(f3, f3_derivative, 1, 3, 64,eps, 100)
        print("Root:", root,"Iterations:",i,"Epsilon:",eps)
    except Exception as err:
        print(repr(err))

print("\n\n-----------------RESULTS FOR SECTANT METHOD-------------------------\n\n")

print("RESULTS FOR FIRST FUNCTION")
for eps in epsilons:
    try:
        root,i = sectant_method(f1,1.5*math.pi, 2*math.pi, 64,eps, 200)
        print("Root:", root,"Iterations:",i,"Epsilon:",eps)
    except Exception as err:
        print(repr(err))
    
print("RESULTS FOR SECOND FUNCTION")
for eps in epsilons:
    try:
        root,i = sectant_method(f2,0, 0.5*math.pi, 64,eps, 200)
        print("Root:", root,"Iterations:",i,"Epsilon:",eps)
    except Exception as err:
        print(repr(err))
    
print("RESULTS FOR THIRD FUNCTION")
for eps in epsilons:
    try:
        root,i = sectant_method(f3,1, 3, 64,eps, 200)
        print("Root:", root,"Iterations:",i,"Epsilon:",eps)
    except Exception as err:
        print(repr(err))
n = 1000

x_1 = np.linspace(1.5*math.pi,2*math.pi,n)
y_1 = [f1(x_1[i]) for i in range(n)]
plt.plot(x_1,y_1)
plt.show()

x_2 = np.linspace(1e-3,0.5*math.pi-1e-3,n)
y_2 = [f2(x_2[i]) for i in range(n)]
plt.plot(x_2,y_2)
plt.show()

x_3 = np.linspace(1,3,n)
y_3 = [f3(x_3[i]) for i in range(n)]
plt.plot(x_3,y_3)
plt.show()

