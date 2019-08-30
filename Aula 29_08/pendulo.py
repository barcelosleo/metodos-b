import matplotlib.pyplot as plt
import math

theta0 = 1.5
omega0 = 0
g = 10
h = 0.01
L = 1
maxT = 20
N = 100
step = (maxT / N)
t = 0

theta_N = theta0
omega_N = omega0
alpha = lambda theta: (-g / L) * math.sin(theta)

lista_theta = []
lista_tempos = []

# Velocity-Verlet
while t <= maxT:
	alpha_N = alpha(theta_N)
	theta_N1 = theta_N + omega_N * h + (alpha_N / 2) * (h ** 2)
	alpha_N1 = alpha(theta_N1)
	omega_N1  = omega_N + ((alpha_N + alpha_N1) / 2) * h
	t += h

	lista_theta.append(theta_N1)
	lista_tempos.append(t)

	theta_N = theta_N1
	omega_N = omega_N1

plt.plot(lista_tempos, lista_theta)

lista_theta = []
lista_tempos = []

theta_N_anterior = theta0

theta_N = theta_N_anterior + omega0 * h + (alpha(theta_N_anterior) / 2) * h ** 2

# Verlet
while t <= maxT:
	alpha_N = alpha(theta_N)
	theta_N1 = 2 * theta_N - (theta_N_anterior) + alpha_N * h ** 2
	t += h

	lista_theta.append(theta_N1)
	lista_tempos.append(t)

	theta_N = theta_N1

	omega_N = omega_N1

plt.plot(lista_tempos, lista_theta)


plt.show()