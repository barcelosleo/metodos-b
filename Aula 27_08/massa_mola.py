import matplotlib.pyplot as plt
import math

v0 = 0 # m/s
x0 = 2 # m
dt = 1e-2
m = 1 # Kg
k = 3 # {}

# Cálculo da energia
energia = lambda v, x: (0.5*m*v**2 + 0.5*k*x**2)

tMax = 10
passos = 200

N = (tMax/passos)

EC_Xn = E_Xn = Xn = x0

EC_Vn = E_Vn = Vn = v0
E0 = energia(Vn, Xn)

omega = (k/m)

tempos = []
lista_x_E = []
lista_x_EC = []
lista_v_E = []
lista_v_EC = []
lista_energias_E = []
lista_energias_EC = []

i = 1
t = 0

while t <= tMax:
	E_Vn1 = E_Vn - omega*E_Xn*dt
	EC_Vn1 = EC_Vn - omega*EC_Xn*dt

	E_Xn1 = E_Xn + E_Vn*dt
	EC_Xn1 = EC_Xn + EC_Vn1*dt

	t = i * dt

	E_Vn = E_Vn1
	EC_Vn = EC_Vn1
	E_Xn = E_Xn1
	EC_Xn = EC_Xn1

	tempos.append(t)
	lista_x_E.append(E_Xn1)
	lista_x_EC.append(EC_Xn1)
	lista_v_E.append(E_Vn1)
	lista_v_EC.append(EC_Vn1)
	lista_energias_E.append(energia(E_Vn1, E_Xn1))
	lista_energias_EC.append(energia(EC_Vn1, EC_Xn1))

	i += 1
plt.subplot(2, 2, 1)
# plt.plot(tempos, lista_x_E)
plt.plot(tempos, lista_x_EC)
plt.plot(tempos, lista_v_EC)
plt.legend(['x(m)', 'v(m/s)'])
plt.ylabel('x(t),v(t)')
plt.xlabel('t')

plt.subplot(2, 2, 2)
plt.plot(tempos, lista_energias_E)
plt.plot(tempos, lista_energias_EC)
plt.legend(['Euler', 'Euler-Crommer'])
plt.ylabel('E(t)')
plt.xlabel('t')

plt.subplot(2, 2, 3)
plt.plot(lista_x_EC, lista_v_EC)
plt.legend(['Euler-Crommer'])
plt.ylabel('v(t)')
plt.xlabel('x(t)')

plt.subplot(2, 2, 4)
plt.plot(lista_x_E, lista_v_E)
plt.legend(['Euler'])
plt.ylabel('v(t)')
plt.xlabel('x(t)')

plt.show()