import matplotlib.pyplot as plt
import math

theta0 = 1.5
omega0 = 0
g = 10
m = 1
h = 0.01
L = 1
maxT = 20
N = 100
step = (maxT / N)
t = 0
alpha = lambda theta: (-(m * g) / L) * math.sin(theta)
energia = lambda omega: (m * (omega * L) ** 2) / 2

E0 = energia(omega0)

# ------------------------------------------ Velocity-Verlet ------------------------------------------ #

theta_N = theta0
omega_N = omega0

lista_theta = []
lista_omega = []
lista_energia = []
lista_tempos = []

while t <= maxT:
	alpha_N = alpha(theta_N)
	theta_N1 = theta_N + omega_N * h + (alpha_N / 2) * (h ** 2)
	alpha_N1 = alpha(theta_N1)
	omega_N1  = omega_N + ((alpha_N + alpha_N1) / 2) * h
	t += h

	lista_theta.append(theta_N1)
	lista_omega.append(omega_N1)
	lista_energia.append(energia(omega_N1))
	lista_tempos.append(t)

	theta_N = theta_N1
	omega_N = omega_N1

plt.subplot(2, 2, 1)
plt.ylabel(r'$ \theta(t) $')
plt.xlabel('t')
plt.plot(lista_tempos, lista_theta)
plt.subplot(2, 2, 2)
plt.ylabel(r'$ \omega(t) $')
plt.xlabel('t')
plt.plot(lista_tempos, lista_omega)
plt.subplot(2, 2, 3)
plt.ylabel(r'$ \omega(t) $')
plt.xlabel('t')
plt.plot(lista_tempos, [(e - E0) for e in lista_energia])
plt.subplot(2, 2, 4)
plt.ylabel(r'$ \omega(t) $')
plt.xlabel('t')
plt.plot(lista_tempos, lista_energia)

# ------------------------------------------ Verlet ------------------------------------------ #

# lista_theta = []
# lista_omega = []
# lista_energia = []
# lista_tempos = []

# theta_N_anterior = theta0

# theta_N = theta_N_anterior + omega0 * h + (alpha(theta_N_anterior) / 2) * h ** 2

# t = 0

# while t <= maxT:
# 	alpha_N = alpha(theta_N)
# 	theta_N1 = 2 * theta_N - (theta_N_anterior) + alpha_N * h ** 2
# 	t += h

# 	lista_theta.append(theta_N1)
# 	lista_omega.append(omega_N1)
# 	lista_energia.append(energia(omega_N1))
# 	lista_tempos.append(t)

# 	theta_N_anterior = theta_N
# 	theta_N = theta_N1

# plt.subplot(2, 2, 1)
# plt.ylabel(r'$ \theta(t) $')
# plt.xlabel('t')
# plt.plot(lista_tempos, lista_theta)
# plt.subplot(2, 2, 2
# plt.ylabel(r'$ \omega(t) $')
# plt.xlabel('t'))
# plt.plot(lista_tempos, lista_omega)

# ------------------------------------------ Euler ------------------------------------------ #

theta_N = theta0
omega_N = omega0

lista_theta = []
lista_omega = []
lista_energia = []
lista_tempos = []

t = 0

while t <= maxT:
	alpha_N = alpha(theta_N)
	omega_N1 = omega_N + alpha_N * h
	theta_N1 = theta_N + omega_N * h
	t += h

	lista_theta.append(theta_N1)
	lista_omega.append(omega_N1)
	lista_energia.append(energia(omega_N1))
	lista_tempos.append(t)

	theta_N = theta_N1
	omega_N = omega_N1

plt.subplot(2, 2, 1)
plt.ylabel(r'$ \theta(t) $')
plt.xlabel('t')
plt.plot(lista_tempos, lista_theta)
plt.subplot(2, 2, 2)
plt.ylabel(r'$ \omega(t) $')
plt.xlabel('t')
plt.plot(lista_tempos, lista_omega)
plt.subplot(2, 2, 3)
plt.ylabel(r'$ \omega(t) $')
plt.xlabel('t')
plt.plot(lista_tempos, [(e - E0) for e in lista_energia])
plt.subplot(2, 2, 4)
plt.ylabel(r'$ \omega(t) $')
plt.xlabel('t')
plt.plot(lista_tempos, lista_energia)

# ------------------------------------------ Euler-Cromer ------------------------------------------ #

theta_N = theta0
omega_N = omega0

lista_theta = []
lista_omega = []
lista_energia = []
lista_tempos = []

t = 0

while t <= maxT:
	alpha_N = alpha(theta_N)
	omega_N1 = omega_N + alpha_N * h
	theta_N1 = theta_N + omega_N1 * h
	t += h

	lista_theta.append(theta_N1)
	lista_omega.append(omega_N1)
	lista_energia.append(energia(omega_N1))
	lista_tempos.append(t)

	theta_N = theta_N1
	omega_N = omega_N1

plt.subplot(2, 2, 1)
plt.ylabel(r'$ \theta(t) $')
plt.xlabel('t')
plt.plot(lista_tempos, lista_theta)
plt.legend(['Velocity-Verlet', 'Euler', 'Euler-Crommer'])
plt.subplot(2, 2, 2)
plt.ylabel(r'$ \omega(t) $')
plt.xlabel('t')
plt.plot(lista_tempos, lista_omega)
plt.subplot(2, 2, 3)
plt.ylabel(r'$ \omega(t) $')
plt.xlabel('t')
plt.plot(lista_tempos, [(e - E0) for e in lista_energia])
plt.subplot(2, 2, 4)
plt.ylabel(r'$ \omega(t) $')
plt.xlabel('t')
plt.plot(lista_tempos, lista_energia)
plt.legend(['Velocity-Verlet', 'Euler', 'Euler-Crommer'])


plt.show()