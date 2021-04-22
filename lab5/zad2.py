import math
from mpmath import mp


def newton_method(f,derivative,a,b,precision,eps,max_iter):
    mp.dps = precision
    i = 0
    x = mp.mpf(a) + (mp.mpf(b)-mp.mpf(a))/2

    if mp.sign(f(a)) == mp.sign(f(b)):
        raise Exception("Function has no root place")
    
    last_val = float("inf")
    while abs(mp.mpf(f(x)) - mp.mpf(last_val)) > mp.mpf(eps) and i < max_iter:
        last_val = f(x)
        x = x - (mp.mpf(f(x)) / mp.mpf(derivative(x)))
        i+=1
    if i == max_iter:
        print("Max iterations reached")

    return x,i 
