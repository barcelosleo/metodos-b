import matplotlib.pyplot as plt
import math

def rk2_ralston(x0, t0, h, tMax, f):
	x = x0
	t = t0

	lista_x = [x0]
	lista_t = [t0]

	i = 1

	N = (tMax - t0) / h

	while t < tMax:
		k1 = f(t, x)
		k2 = f(t + (3/4) * h, x + (3/4) * k1 * h)
		x = x + ((1/3) * k1 + (2/3) * k2) * h

		t = i * h

		lista_t.append(t)
		lista_x.append(x)

		i += 1

	return {
		'x': lista_x,
		't': lista_t,
	}

def rk2_ponto_central(x0, t0, h, tMax, f):
	x = x0
	t = t0

	lista_x = [x0]
	lista_t = [t0]

	i = 1

	N = (tMax - t0) / h

	while t < tMax:
		k1 = f(t, x)
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

def rk2_heun(x0, t0, h, tMax, f):
	x = x0
	t = t0

	lista_x = [x0]
	lista_t = [t0]

	i = 1

	N = (tMax - t0) / h

	while t < tMax:
		k1 = f(t, x)
		k2 = f(t + h, x + k1 * h)
		x = x + (k1 + k2) * h * (1/2)

		t = i * h

		lista_t.append(t)
		lista_x.append(x)

		i += 1

	return {
		'x': lista_x,
		't': lista_t,
	}

def f(t, x):
	return x - t ** 2 + 1

def main():
	x0 = 0.5
	t0 = 0
	h = 0.01
	tMax = 2
	resultados = rk2_ponto_central(x0, t0, h, tMax, f)

	analitico = lambda t: (t + 1) ** 2 - 0.5 * math.exp(t)

	plt.plot(resultados['t'], resultados['x'], '.')
	plt.plot(resultados['t'], [analitico(t) for t in resultados['t']])

	plt.legend(['RK2-Ponto-Central', 'Analítico'])

	plt.show()

	ordem_hMin = -5
	ordem_hMax = 1

	xCalc = analitico(2)

	lista_h = []
	lista_ralston = []
	lista_heun = []
	lista_ponto_central = []

	for ordem_h in range(ordem_hMin, ordem_hMax):
		h = 1 * 10 ** ordem_h
		ralston = rk2_ralston(x0, t0, h, tMax, f)
		ponto_central = rk2_ponto_central(x0, t0, h, tMax, f)
		heun = rk2_heun(x0, t0, h, tMax, f)

		print('-----------------------')
		print(ralston['t'][-1])
		print(ponto_central['t'][-1])
		print(heun['t'][-1])
		print('-----------------------')

		lista_h.append(h)
		lista_ralston.append(abs(xCalc - ralston['x'][-1]))
		lista_ponto_central.append(abs(xCalc - ponto_central['x'][-1]))
		lista_heun.append(abs(xCalc - heun['x'][-1]))

	plt.plot(lista_h, lista_ralston, '.-')
	plt.plot(lista_h, lista_ponto_central, '.-')
	plt.plot(lista_h, lista_heun, '.-')

	plt.yscale('log')
	plt.xscale('log')

	plt.legend(['Ralston', 'Ponto Central', 'Heun'])

	plt.show()


main()


