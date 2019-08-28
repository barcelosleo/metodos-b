import matplotlib.pyplot as plt
import math

v0 = 1 # m/s
x0 = 2 # m
dt = 1e-2
m = 1 # Kg
k = 3 # {}

tMax = 120
passos = 200

N = (tMax/passos)

EC_Xn = E_Xn = Xn = x0

EC_Vn = E_Vn = Vn = v0
E0 = 0.5*m*Vn**2 + 0.5*k*Xn**2

omega = (k/m)

tempos = []
lista_x_E = []
lista_x_EC = []
lista_v_E = []
lista_v_EC = []

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

	i += 1

plt.plot(tempos, lista_x_E)
plt.plot(tempos, lista_x_EC)
# plt.plot(tempos, lista_v)

plt.legend(['Euler', 'Euler Cromer'])

plt.show()