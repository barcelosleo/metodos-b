import matplotlib.pyplot as plt
import math
import time

# df/dt = -x/tau

dt = 1/7
tau = 1
x0 = 1e6
tempo = 0

tempos = []
euler_implicito = []
euler_explicito = []

i_Xn = x0
e_Xn = x0

i = 1

while tempo <= 10:
	e_Xn1 = e_Xn + dt * (-e_Xn / tau)
	i_Xn1 = i_Xn / (1 + (dt / tau))

	tempo = i * dt

	tempos.append(tempo)
	euler_explicito.append(e_Xn1)
	euler_implicito.append(i_Xn1)

	e_Xn = e_Xn1
	i_Xn = i_Xn1

	i += 1

plt.plot(tempos, euler_explicito)
plt.plot(tempos, euler_implicito)
plt.plot(tempos, [math.exp(-i/tau) * x0 for i in tempos])

plt.title(f'dt = {dt}')

plt.legend(['Euler Explícito', 'Euler Implícito', 'x_{0}e^{-x/tau}'])

plt.show()