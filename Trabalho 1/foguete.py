import matplotlib.pyplot as plt
import math
from scipy import constants

G = 9.8
C = 3403
r = 5
ro = 1141

# Propelente: Oxigênio Líquido
A = math.pi * r ** 2
Pt = 101325 * 1 # Pa
Tt = 275 # K
gama = 1.4 #

momento = lambda m, v: m * v

def dMdT_(A, Pt, Tt, gama, M = 1):
	R = constants.Avogadro
	return ((A * Pt) / Tt ** (1 / 2)) * (gama / R) ** (1 / 2) * M * (1 + ((gama - 1) / 2) * M ** 2) ** (-(gama + 1) / 2 * (gama - 1))

dMdt = dMdT_(A, Pt, Tt, gama)

def velocity_verlet(x0, v0, t0, m0, p, p0, A, me, h):
	x = x0
	v = v0
	t = t0
	m = m0

	dados = {
		't': [t],
		'x': [x],
		'v': [v],
		'm': [m],
		'a': [0],
		'momento': [momento(m, v)],
	}

	i = 1

	# a = lambda M: (((p - p0) * A) / M) - G + (C * dMdt) / M

	def a(M):
		return (((p - p0) * A) / M) - G + (C * dMdt) / M

	while m >= me:
		t = i * h # Calculo o tempo seguinte
		m = m - i * dMdt
		a1 = a(m)

		x = x + v * h + (1 / 2) * a1 * h ** 2

		m1 = m - (i + 1) * dMdt
		a2 = a(m1)

		v = v + (a1 + a2) * (h / 2)


		dados['t'].append(t)
		dados['x'].append(x)
		dados['v'].append(v)
		dados['m'].append(m)
		dados['a'].append(a1)
		dados['momento'].append(momento(m, v))

		i += 1

	return dados

def rk2(theta0, omega0, t0, tMax, h, f_a, f_v):
	theta = theta0
	omega = omega0
	t = t0

	dados = {
		't': [t],
		'theta': [theta0],
		'omega': [omega0],
		'momento': [momento(theta, omega)],
	}

	i = 1

	while t < tMax:
		k1_theta = omega
		k1_omega = f(theta)

		k2_theta = omega + k1_omega * (h/2)
		k2_omega = f(theta + k1_theta * (h/2))

		theta = theta + k2_theta * h
		omega = omega + k2_omega * h

		t = i * h

		dados['t'].append(t)
		dados['theta'].append(theta)
		dados['omega'].append(omega)
		dados['momento'].append(momento(theta, omega))

		i += 1

	return dados

def rk4(theta0, omega0, t0, tMax, h, f):
	theta = theta0
	omega = omega0
	t = t0

	dados = {
		't': [t],
		'theta': [theta0],
		'omega': [omega0],
		'momento': [momento(theta, omega)],
	}

	i = 1

	while t < tMax:
		k1_theta = omega
		k1_omega = f(theta)

		k2_theta = omega + k1_omega * (h/2)
		k2_omega = f(theta + k1_theta * (h/2))

		k3_theta = omega + k2_omega * (h/2)
		k3_omega = f(theta + k2_theta * (h/2))

		k4_theta = omega + k3_omega * h
		k4_omega = f(theta + k3_theta * h)

		theta = theta + (h/6) * (k1_theta + 2 * k2_theta + 2 * k3_theta + k4_theta)
		omega = omega + (h/6) * (k1_omega + 2 * k2_omega + 2 * k3_omega + k4_omega)

		t = i * h

		dados['t'].append(t)
		dados['theta'].append(theta)
		dados['omega'].append(omega)
		dados['momento'].append(momento(theta, omega))

		i += 1

	return dados

def main():
	x0 = 0
	v0 = 0
	t0 = 0
	me = 100
	mp = 900
	m0 = me + mp
	h = 0.01

	p = 101325 * 9
	p0 = 101325


	verlet = velocity_verlet(x0, v0, t0, m0, p, p0, A, me, h)

	# v_comp = {
	# 	't': [],
	# 	'x': [],
	# 	'v': [],
	# 	'm': [],
	# 	'a': [],
	# 	'momento': [],
	# }

	# for dado in verlet :


	# plt.plot(verlet['t'], verlet['a'])
	plt.plot(verlet['t'][1:], verlet['a'][1:])
	# plt.plot(verlet['t'], verlet['m'])

	# plt.legend(['Velocidade', 'Altura'])

	plt.show()

print(dMdt)
main()
