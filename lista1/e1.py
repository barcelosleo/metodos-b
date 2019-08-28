import matplotlib.pyplot as plt
import math

x0 = 0
t0 = 0
dt = 10e-3

for x0 in range(-10, 10, 2):
	T = 0
	tempos = []
	lista_x = []
	Xn = x0

	i = 0

	while T <= 10:
		Xn1 = Xn + dt * (1 - Xn)
		T = dt * i

		tempos.append(T)
		lista_x.append(Xn1)

		Xn = Xn1

		i += 1

	plt.plot(tempos, lista_x)

plt.show()