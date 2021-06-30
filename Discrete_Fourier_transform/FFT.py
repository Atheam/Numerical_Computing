import numpy as np
from math import pi
from scipy.fft import fft
import time



def F_n(n):
    return np.array([[np.exp(1j*-2*pi*j*k/n) for j in range(n)] for k in range(n)])

def DFT(x):
    return F_n(x.shape[0]) @ x

def IDFT(y):
    return np.conj(F_n(y.shape[0]) @ np.conj(y)) / y.shape[0]

def FFT(x):
    n = x.shape[0]
    if n == 1:
        return x
    
    F_x_even = FFT(x[::2])
    F_x_odd = FFT(x[1::2])

    m = n//2

    upper = np.zeros(m,dtype = np.complex64)
    lower = np.zeros(m,dtype = np.complex64)
    for k in range(m):
        omega = np.exp(1j*-2*pi*k/n)
        upper[k] = F_x_even[k] + omega*F_x_odd[k]
        lower[k] = F_x_even[k] - omega*F_x_odd[k]
    return np.concatenate((upper,lower))


n = 4

x = np.random.uniform(0,10,n)

print("ZADANIE 1")
print("Sprawdzanie poprawnosci dzialania")
print("x przed transformacjami")
print(x)
print("x po transformacjach x - > DFT -> IDFT -> x ")
print(IDFT(DFT(x)))


n = 1024

print("Czasy dzialania dla n =",n)

x = np.random.uniform(0,10,n)

start = time.time()
DFT(x)
end = time.time()
print("Czas dzialania DFT:",end-start,"s")


start = time.time()
FFT(x)
end = time.time()
print("Czas dzialania FFT:",end-start,"s")

start = time.time()
fft(x)
end = time.time()
print("Czas dzialania fft funkcja biblioteczna:",end-start,"s")













