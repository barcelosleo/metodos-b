import matplotlib.pyplot as plt

def aleatorio():
	# Nao altere esta funcao!!!
	a = 16807
	m = 2147483647

	aleatorio.x = a*aleatorio.x % m
	y = 1.0*aleatorio.x/m
	return y
aleatorio.x = 947236

def primeira_parte():
	x = []
	y = []
	medias = []
	medias_y = []
	desvios = []
	desvios_y = []
	N = 10000
	lista = range(1, N + 1)

	for i in lista:
		x.append(aleatorio() * 100)
		medias.append(sum(x)/i)
		desvios.append(((1 / i) * sum([(xi - medias[-1]) ** 2 for xi in x])) ** (1/2))

	cont = 0
	soma_y = 0
	for xi in x:
		if cont <= 20:
			soma_y += xi
			cont += 1
		else:
			y.append(soma_y / 20)
			medias_y.append(sum(y)/len(y))
			desvios_y.append(((1 / len(y)) * sum([(yi - medias_y[-1]) ** 2 for yi in y])) ** (1/2))
			cont = 0
			soma_y = 0

	plt.subplot(3, 2, 1)
	plt.plot(lista, medias)
	plt.subplot(3, 2, 3)
	plt.plot(lista, desvios)
	plt.subplot(3, 2, 5)
	plt.hist(x, bins=100)

	plt.subplot(3, 2, 2)
	plt.plot(range(1, len(y) + 1), y)
	plt.subplot(3, 2, 4)
	plt.plot(range(1, len(y) + 1), desvios_y)
	plt.subplot(3, 2, 6)
	plt.hist(y, bins=100)
	plt.show()

def segunda_parte():
	y = []


def main():
	primeira_parte()

main()