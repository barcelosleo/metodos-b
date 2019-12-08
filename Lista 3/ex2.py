import math
import matplotlib.pyplot as plt

def aleatorio():
	# Nao altere esta funcao!!!
	a = 16807
	m = 2147483647

	aleatorio.x = a*aleatorio.x % m
	y = 1.0*aleatorio.x/m
	return y
aleatorio.x = 947236

N = (math.exp(-1) - math.exp(-7))

def distribuicao_exp(R):
	return -math.log(math.exp(-1) - (N * R))

def p(x):
	return math.exp(-x)

def main():
	n = 10000
	x = []
	for i in range(n):
		x.append(distribuicao_exp(aleatorio()))

	plt.subplot(2, 1, 1)
	plt.hist(x, bins=100)
	plt.subplot(2, 1, 2)
	plt.plot([(i / n) for i in range(n)], [p(i / n) for i in range(n)])

	plt.show()
main()
