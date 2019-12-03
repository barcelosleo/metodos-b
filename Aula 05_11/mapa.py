import matplotlib.pyplot as plt

def f(lamb, x):
	return 4 * lamb * x * (1 - x)

def mapa(x0, lamb):
	x = x0

	dados = []

	for i in range(300):
		x = f(lamb, x)

	for i in range(400):
		x = f(lamb, x)
		dados.append(x)

	return dados

def main():
	lamb0 = 0.72
	lamb1 = 1
	h = (lamb1 - lamb0) / 400
	x0 = 0.5

	plot = {
		'lambda': [],
		'x': []
	}

	for i in range(400):
		lamb = lamb0 + i * h
		dados = mapa(x0, lamb)
		plot['lambda'] += [lamb for i in range(400)]
		plot['x'] += dados

	plt.plot(plot['lambda'], plot['x'], '.', markersize=1)
	plt.show()

main()
