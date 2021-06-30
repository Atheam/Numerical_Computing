import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft


n = 5
freq = [10,20,40,80,160]
signals = []
samples = 500
domain = np.linspace(0,1,samples)    
for f in freq:
    signal = np.sin(2*np.pi*f*domain)
    signals.append((domain,signal))

#punkt a
signals_sum_a = signals[0][1] + signals[1][1] + signals[2][1] + signals[3][1] + signals[4][1]

#punkt b
signals_sum_b = []
i = 0
for k in range(samples):
    if k % (samples//n) == 0 and k != 0:
        i+=1
    signals_sum_b.append(signals[i][1][k])


signals_sum_b = np.array(signals_sum_b)


plt.plot(domain,signals_sum_a)
plt.title("Suma pieciu sygnałow o roznych czestotliwosciach")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.show()

plt.plot(abs(fft(signals_sum_a)))
plt.title("Widmo sygnału z punktu a")
plt.xlabel("Czestotliwosc")
plt.ylabel("Amplituda")
plt.show()

plt.plot(np.real((fft(signals_sum_a))))
plt.title("Czesc rzeczywista sygnalu z punktu a")
plt.xlabel("Czestotliwosc")
plt.ylabel("Amplituda")
plt.show()

plt.plot(np.imag((fft(signals_sum_a))))
plt.title("Czesc urojona sygnalu z punktu a")
plt.xlabel("Czestotliwosc")
plt.ylabel("Amplituda")
plt.show()


plt.plot(domain,signals_sum_b)
plt.title("Piec sygnalow o różnych czestotliwościach \"sklejone\" razem")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.show()

plt.plot(abs(fft(signals_sum_b)))
plt.title("Widmo sygnału z punktu b")
plt.xlabel("Czestotliwosc")
plt.ylabel("Amplituda")
plt.show()

plt.plot(np.real((fft(signals_sum_b))))
plt.title("Czesc rzeczywista sygnalu z punktu b")
plt.xlabel("Czestotliwosc")
plt.ylabel("Amplituda")
plt.show()

plt.plot(np.imag((fft(signals_sum_b))))
plt.title("Czesc urojona sygnalu z punktu b")
plt.xlabel("Czestotliwosc")
plt.ylabel("Amplituda")
plt.show()


