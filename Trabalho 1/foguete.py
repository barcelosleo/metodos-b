import matplotlib.pyplot as plt
import math

a = 2
G = 9.8
C = 20
M0 = 1000
dMdt = -a * M0

def momento(m, v):
	return m * v

def f_a(m):
  return - (C/m) * dMdt - G

def f_v(t, m):
  return - (G * t) + (C * math.log(M0/m))

def velocity_verlet(x0, v0, t0, m0, combustivel, h, f_a, f_v):
	x = x0
	v = v0
	t = t0
	m = m0

	dados = {
		't': [t],
		'x': [x],
		'v': [v],
		'm': [m],
		'momento': [momento(m, v)],
	}

	i = 1

	while combustivel > 0:
		t = i * h # Calculo o tempo seguinte
		m = m0 * (1 - a * t) # Calculo o quanto de massa será ejetado
		combustivel -= m # Tira a massa ejetada do combustivel

		a1 = f_a(m) # Calculo a primeira aceleração


		v = v + (h ** 2) * ((a1 + a2) / 2)
		x = x + v * h + (a / 2) * h ** 2


		alpha = f(theta)
		theta = theta + omega * h + (alpha / 2) * h ** 2
		alpha2 = f(theta)
		omega = omega + ((alpha + alpha2) / 2) * h

		t = i * h

		dados['t'].append(t)
		dados['theta'].append(theta)
		dados['omega'].append(omega)
		dados['momento'].append(momento(theta, omega))

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

def f(theta):
	return (-G / L) * math.sin(theta)

def main():
  pass