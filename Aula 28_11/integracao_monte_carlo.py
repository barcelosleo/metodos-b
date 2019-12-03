from random import seed, random
import math

def f(x):
	return math.sin(x)

def media(funcao, N, numeros_aleatorios):
	sum = 0
	for na in numeros_aleatorios:
		sum += funcao(na)

	return (1 / N) * sum

def integral(V, funcao, N, numeros_aleatorios):
	media_f = media(funcao, N, numeros_aleatorios)
	media_f_ao_quadrado = media(lambda x: funcao(x) * funcao(x), N, numeros_aleatorios)

	return (
		(V * media_f),
		(V * (((media_f_ao_quadrado - (media_f ** 2)) / N) ** (1/2)))
	)


def main():
	seed(1)
	N = 200000
	x = 2 * math.pi
	I = integral(x, f, N, [random() * x for i in range(N)])
	print(I[0], '±', I[1])

main()