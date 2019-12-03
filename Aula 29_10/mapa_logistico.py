import matplotlib.pyplot as plt
import math

def f(x, lamb):
	return 4 * lamb * x * (1 - x)

def mapa(lamb, x0, max_x, h):
	xn = x0

	dados = {
		'xn': [],
		'xn1': []
	}

	i = 1

	while xn <= max_x:
		dados['xn'].append(xn)
		xn1 = f(xn, lamb)
		dados['xn1'].append(xn1)

		xn = i * h
		i += 1

	return dados


def main():
	lamb = 0.5
	x_min = 0
	x_max = 1
	h = 0.01

	m = mapa(0.5, 0, 1, 0.01)

	plt.plot(m['xn'], m['xn1'])
	plt.grid(True)

	plt.show()

main()