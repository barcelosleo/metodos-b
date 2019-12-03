import matplotlib.pyplot as plt
import math
import numpy as np
import sys

def graficos_X_n(lambs, x0s):
	for lamb in lambs:
		legends = []
		plt.title(f'$\lambda = {lamb}$')
		for x0 in x0s:
			xs = [x0]
			xn = [0]
			x = x0
			legends.append(f'$x_0 = {x0}$')
			for n in range(1, 11):
				x = mapa_logistico(x, lamb)
				xs.append(x)
				xn.append(n)

			plt.plot(xn, xs, marker='^', linestyle=':')

		plt.legend(legends)
		figManager = plt.get_current_fig_manager()
		figManager.window.showMaximized()
		plt.ylabel('$x_n$')
		plt.xlabel('$n$')
		plt.show()

def grafico_bifurcacao():
	h = (1 - 0.72) / 400

	lamb = 0.72

	lista_x = []
	lista_lamb = []
	lista_lamb_lyap = []
	lista_lyap = []

	while lamb <= 1:
		lamb += h

		x = 0.1

		lista_x_local = []

		for i in range(700):
			x = mapa_logistico(x, lamb)

		for i in range(300):
			x = mapa_logistico(x, lamb)
			lista_x.append(x)
			lista_x_local.append(x)
			lista_lamb.append(lamb)

		lista_lamb_lyap.append(lamb)
		lista_lyap.append(expoenteLyapunov(lista_x_local, lamb))

	plt.subplot(2, 1, 1)
	plt.plot(lista_lamb, lista_x, '.', markersize=1)
	plt.ylabel('$x_{n+1}$')
	plt.xlabel('$\lambda$')


	plt.subplot(2, 1, 2)
	plt.plot(lista_lamb_lyap, lista_lyap, color="red")

	figManager = plt.get_current_fig_manager()
	figManager.window.showMaximized()
	plt.show()

def grafico_teia(lambs):
	for lamb in lambs:
		x = 0.5
		xs = [x]
		ys = [0]

		xMax = 1

		h = xMax/100

		i = 0

		n = 0

		while n <= xMax:
			n = i * h

			xs.append(x)
			x = mapa_logistico(x, lamb)
			ys.append(x)

			xs.append(x)
			ys.append(x)

			i += 1

		reta = np.arange(0, xMax, h)

		plt.plot(reta, reta)
		plt.plot(reta, [mapa_logistico(xn, lamb) for xn in reta])

		for i in range(i):
			plt.arrow(xs[i], ys[i], xs[i + 1] - xs[i], ys[i + 1] - ys[i], width=0.001, head_length=0.0001, color='red', linestyle=':', linewidth=0.01)

		figManager = plt.get_current_fig_manager()
		figManager.window.showMaximized()

		plt.legend([r'$y = x$', r'$f(x) = 4 \lambda x_n (1 - x_n)$'])
		plt.ylabel(r'$x_{n+1}$')
		plt.xlabel(r'$x_n$')
		plt.title(f"$\lambda = {lamb}$")
		plt.show()

def grafico_recorrencia(lambs):
	for lamb in lambs:
		x = 0.5
		xs = [x]
		E = 1e-4

		if lamb == 0.99:
			c = 1000
		else:
			c = 100

		xMax = 1

		h = xMax/c

		i = 0

		n = 0


		while n <= xMax:
			n = i * h

			x = mapa_logistico(x, lamb)
			xs.append(x)

			i += 1

		mr_x = []
		mr_y = []

		for i in range(c):
			for j in range(c):
				if abs(xs[i] - xs[j]) < E:
					mr_x.append(i)
					mr_y.append(j)

		plt.plot(mr_x, mr_y, 'ro', markersize=1.5)

		figManager = plt.get_current_fig_manager()
		figManager.window.showMaximized()

		plt.ylabel(r'$i$')
		plt.xlabel(r'$j$')
		plt.title(f"$\lambda = {lamb}$")
		plt.show()

def expoenteLyapunov(x, lamb):
	sum = 0
	n = len(x)
	for i in range(n):
		sum += math.log(abs(df(x[i], lamb)))

	return (1 / n) * sum

def df(x, lamb):
	return 4 * lamb * (1 - 2 * x)

def mapa_logistico(x, lamb):
	return 4 * lamb * x * (1 - x)

def main():
	lambs = [0.1, 0.4, 0.8, 0.88, 0.99]
	x0s = [0.01, 0.25, 0.51, 0.99]

	graficos_X_n(lambs, x0s)
	grafico_bifurcacao()
	grafico_teia(lambs)
	grafico_recorrencia(lambs)

main()