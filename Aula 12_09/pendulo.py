import matplotlib.pyplot as plt
import math

G = 10
L = 1

def energia(theta, omega):
	return G * L * (1 - math.cos(theta)) + (1/2) * L ** 2 * omega ** 2

def velocity_verlet(theta0, omega0, t0, tMax, h, f):
	theta = theta0
	omega = omega0
	t = t0

	dados = {
		't': [t],
		'theta': [theta0],
		'omega': [omega0],
		'energia': [energia(theta, omega)],
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
		dados['energia'].append(energia(theta, omega))

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
		'energia': [energia(theta, omega)],
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
		dados['energia'].append(energia(theta, omega))

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
		'energia': [energia(theta, omega)],
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
		dados['energia'].append(energia(theta, omega))

		i += 1

	return dados

def f(theta):
	return (-G / L) * math.sin(theta)

def main():
	theta0 = 3
	omega0 = 0
	t0 = 0
	tMax = 20
	h = 0.01

	vel_verlet = velocity_verlet(theta0, omega0, t0, tMax, h, f)
	runge_k2 = rk2(theta0, omega0, t0, tMax, h, f)
	runge_k4 = rk4(theta0, omega0, t0, tMax, h, f)
	runge_k4_ = rk4(theta0, omega0, t0, tMax, h * 10, f)

	plt.subplot(2, 2, 1)
	plt.plot(vel_verlet['t'], vel_verlet['theta'])
	plt.plot(runge_k2['t'], runge_k2['theta'], '.')
	plt.plot(runge_k4['t'], runge_k4['theta'], '.')
	plt.plot(runge_k4_['t'], runge_k4_['theta'], '.')

	plt.ylabel(r'$\theta(t)$')
	plt.xlabel('t')

	plt.legend(['Velocity-Verlet', 'RK2', 'RK4 h = 0.01', 'RK4 h = 0.1'])


	plt.subplot(2, 2, 2)
	plt.plot(vel_verlet['t'], vel_verlet['omega'])
	plt.plot(runge_k2['t'], runge_k2['omega'], '.')
	plt.plot(runge_k4['t'], runge_k4['omega'], '.')
	plt.plot(runge_k4_['t'], runge_k4_['omega'], '.')

	plt.ylabel(r'$\omega(t)$')
	plt.xlabel('t')

	plt.legend(['Velocity-Verlet', 'RK2', 'RK4 h = 0.01', 'RK4 h = 0.1'])


	plt.subplot(2, 2, 3)
	plt.plot(vel_verlet['t'], [(vel_verlet['energia'][0] - e)/vel_verlet['energia'][0] for e in vel_verlet['energia']])
	plt.plot(runge_k2['t'], [(runge_k2['energia'][0] - e)/runge_k2['energia'][0] for e in runge_k2['energia']])
	plt.plot(runge_k4['t'], [(runge_k4['energia'][0] - e)/runge_k4['energia'][0] for e in runge_k4['energia']])
	plt.plot(runge_k4_['t'], [(runge_k4_['energia'][0] - e)/runge_k4_['energia'][0] for e in runge_k4_['energia']])

	plt.ylabel(r'$(E_0 - E(t))/E_0$')
	plt.xlabel('t')

	plt.legend(['Velocity-Verlet', 'RK2', 'RK4 h = 0.01', 'RK4 h = 0.1'])


	plt.subplot(2, 2, 4)
	plt.plot(vel_verlet['t'], [abs(vel_verlet['energia'][0] - e)/abs(vel_verlet['energia'][0]) for e in vel_verlet['energia']])
	plt.plot(runge_k2['t'], [abs(runge_k2['energia'][0] - e)/abs(runge_k2['energia'][0]) for e in runge_k2['energia']])
	plt.plot(runge_k4['t'], [abs(runge_k4['energia'][0] - e)/abs(runge_k4['energia'][0]) for e in runge_k4['energia']])
	plt.plot(runge_k4_['t'], [abs(runge_k4_['energia'][0] - e)/abs(runge_k4_['energia'][0]) for e in runge_k4_['energia']])

	plt.ylabel(r'$|(E_0 - E(t))|/|E_0|$')
	plt.xlabel('t')

	plt.yscale('log')

	plt.legend(['Velocity-Verlet', 'RK2', 'RK4 h = 0.01', 'RK4 h = 0.1'])

	plt.show()

main()