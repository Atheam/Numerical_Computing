import math
from mpmath import mp

def sectant_method(f,a,b,precision,eps,max_iter):
    mp.dps = precision  

    if mp.sign(f(a)) == mp.sign(f(b)):
        raise Exception("Function has no root place")
    
    a+=1e-2
    b-=1e-2
    x = mp.mpf(a) - mp.mpf(f(a)) * (mp.mpf(b) - mp.mpf(a)) / (f(b) - f(a))

    i = 0
    while abs(f(x)) > eps and i < max_iter:
        x = mp.mpf(a) - mp.mpf(f(a)) * (mp.mpf(b) - mp.mpf(a)) / (f(b) - f(a))
        if mp.sign(f(a)) != mp.sign(f(x)):
            b = x
        else:
            a = x
        i+=1

    if i == max_iter:
        print("Max iteration reached")

    return x,i









