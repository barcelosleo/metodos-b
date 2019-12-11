import math
import matplotlib.pyplot as plt

N = (math.exp(-1) - math.exp(-7))

def aleatorio():
	# Nao altere esta funcao!!!
	a = 16807
	m = 2147483647

	aleatorio.x = a*aleatorio.x % m
	y = 1.0*aleatorio.x/m
	return y
aleatorio.x = 947236

def distribuicao_exp(R):
	return -math.log(math.exp(-1) - (N * R))

def p(x):
	return math.exp(-x)

def media(dados):
	return sum(dados) / len(dados)

def desvio_padrao(dados):
	med = media(dados)
	return ((1 / len(dados)) * sum([(xi - med) ** 2 for xi in dados]) ) ** (1 / 2)

def histograma(dados, bins, normalized = False):
	maximo = max(dados)
	minimo = min(dados)

	histograma = [0] * bins

	tamanho_classe = (maximo - minimo) / bins

	for xi in dados:
		classe = math.floor(xi - minimo)
		histograma[classe] += 1

	plt.bar([minimo + (i * tamanho_classe) for i in range(bins)], histograma, width=tamanho_classe)





def main():
	n = 10000
	x = []
	for i in range(n):
		x.append(distribuicao_exp(aleatorio()))

	plt.hist(x, bins=100, density=1)
	plt.plot(range(1, 8), [p(i) for i in range(1, 8)])
	plt.legend(['$P(x)$', 'Histograma'])
	plt.show()
main()
