import matplotlib.pyplot as plt
import math

def velocity_verlet(theta0, omega0, t0, tMax, h, f):
	theta = theta0
	omega = omega0
	t = t0

	dados = {
		't': [t],
		'theta': [theta0],
		'omega': [omega0],
	}

	i = 1

	while t < tMax:
		alpha = f(theta)
		theta = theta + omega * h + (alpha / 2) * h ** 2
		alpha2 = f(theta)
		omega = omega + ((alpha + alpha2) / 2) * h

		t = i * h

		dados['t'].append(t)
		dados['theta'].append(theta)
		dados['omega'].append(omega)

		i += 1

	return dados

def rk2(theta0, omega0, t0, tMax, h, f):
	theta = theta0
	omega = omega0
	t = t0

	dados = {
		't': [t],
		'theta': [theta0],
		'omega': [omega0],
	}

	i = 1

	while t < tMax:
		k1_theta = f(t, x)
		k2 = f(t + (1/2) * h, x + (1/2) * k1 * h)
		x = x + k2 * h

		t = i * h

		lista_t.append(t)
		lista_x.append(x)

		i += 1

	return {
		'x': lista_x,
		't': lista_t,
	}

def f(theta):
	g = 10
	L = 1
	return (-g / L) * math.sin(theta)

def main():
	theta0 = 1.5
	omega0 = 0
	g = 10
	t0 = 0
	tMax = 20
	h = 0.01

	vel_verlet = velocity_verlet(theta0, omega0, t0, tMax, h, f)

	plt.plot(vel_verlet['t'], vel_verlet['theta'])

	plt.show()

main()