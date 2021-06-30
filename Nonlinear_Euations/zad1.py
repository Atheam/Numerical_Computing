from mpmath import mp
import math

def bisection_method(f,a,b,precision,eps):
    mp.dps = precision
    
    if mp.sign(f(a)) == mp.sign(f(b)):
        raise Exception("Function has no root place")
    i = 0
    c = a
    while b-a > eps and abs(f(c)) > eps :
        c = mp.mpf(a) + (mp.mpf(b)-mp.mpf(a))/2
        if mp.sign(f(a)) != mp.sign(f(c)):
            b = c
        else:
            a = c
        i+=1
    
    return c,i











    

