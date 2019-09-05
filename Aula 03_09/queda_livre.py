import matplotlib.pyplot as plt
import math

def euler(v0, x0, t0, h, tMax, gama, aceleration):
	v = v0
	x = x0
	t = t0

	lista_v = []
	lista_x = []
	lista_t = []

	while x >= 0:
		x = x + v * h
		if (x <= 0):
			v = 0
		else:
			v = v + aceleration(v, gama) * h

		t += h

		lista_x.append(x)
		lista_v.append(v)
		lista_t.append(t)

	return {'t': lista_t, 'x': lista_x, 'v': lista_v}

def euler_crommer(v0, x0, t0, h, tMax, gama, aceleration):
	v = v0
	x = x0
	t = t0

	lista_v = []
	lista_x = []
	lista_t = []

	while x >= 0:
		if (x <= 0):
			v = 0
		else:
			v = v + aceleration(v, gama) * h

		x = x + v * h
		t += h

		lista_x.append(x)
		lista_v.append(v)
		lista_t.append(t)

	return {'t': lista_t, 'x': lista_x, 'v': lista_v}

def velocity_verlet(v0, x0, t0, h, tMax, gama, aceleration):
	v = v0
	x = x0
	t = t0

	lista_v = []
	lista_x = []
	lista_t = []

	while x >= 0:
		x = x + v * h + (aceleration(v, gama) / 2) * h ** 2
		if (x <= 0):
			v = 0
		else:
			v = v + velocity_verlet_Vn(v, gama, h) * h

		t += h

		lista_x.append(x)
		lista_v.append(v)
		lista_t.append(t)

	return {'t': lista_t, 'x': lista_x, 'v': lista_v}

def aceleration(v, gama):
	g = 9.8 # m/s
	m = 1 # Kg
	return (-g - (gama / m) * v)

def velocity_verlet_Vn(v, gama, h):
	g = 9.8 # m/s
	m = 1 # Kg
	return (v - g * h - (gama/(2 * m)) * v * h)/(1 + (gama/(2 * m)) * h)

def main():
	v0 = 0 # m/s
	x0 = 1000 # m
	t0 = 0 # s
	h = 0.1 # s
	tMax = 110 # s
	gama = 0

	pontos_euler = euler(v0, x0, t0, h, tMax, gama, aceleration)
	pontos_euler_crommer = euler_crommer(v0, x0, t0, h, tMax, gama, aceleration)
	pontos_velocity_verlet = velocity_verlet(v0, x0, t0, h, tMax, gama, aceleration)

	# plt.scatter(pontos_euler['t'], pontos_euler['x'], marker='.', c=[v for v in pontos_euler['v']])
	# plt.scatter(pontos_euler_crommer['t'], pontos_euler_crommer['x'], marker='.', c=[v for v in pontos_euler_crommer['v']])
	# plt.scatter(pontos_velocity_verlet['t'], pontos_velocity_verlet['x'], marker='.', c=[v for v in pontos_velocity_verlet['v']])
	# plt.colorbar()

	plt.subplot(1, 2, 1)
	plt.plot(pontos_euler['t'], pontos_euler['x'])
	plt.plot(pontos_euler_crommer['t'], pontos_euler_crommer['x'])
	plt.plot(pontos_velocity_verlet['t'], pontos_velocity_verlet['x'])
	plt.ylabel('h(m)')
	plt.xlabel('t(s)')
	plt.legend(['Euler', 'Euler-Crommer', 'Velocity-Verlet'])

	plt.subplot(1, 2, 2)
	plt.plot(pontos_euler['t'], pontos_euler['v'])
	plt.plot(pontos_euler_crommer['t'], pontos_euler_crommer['v'])
	plt.plot(pontos_velocity_verlet['t'], pontos_velocity_verlet['v'])
	plt.ylabel('v(m/s)')
	plt.xlabel('t(s)')
	plt.legend(['Euler', 'Euler-Crommer', 'Velocity-Verlet'])


	plt.show()

main()