import math
import matplotlib.pyplot as plt
# import PyGnuplot as gnu

########################################################################
### Funcao aleatorio() gera um numero pseudo-aleatorio uniformemente no
### intervalo [0,1)
########################################################################
def aleatorio():
	# Nao altere esta funcao!!!
	a = 16807
	m = 2147483647

	aleatorio.x = a*aleatorio.x % m
	y = 1.0*aleatorio.x/m
	return y
aleatorio.x = 947236

def media(dados):
	return sum(dados) / len(dados)

def desvpad(dados):
	med = media(dados)
	return ((1 / (len(dados) - 1)) * sum([(xi - med) ** 2 for xi in dados]) ) ** (1 / 2)

def distribuicao_(R):
    return (20 / math.pi) * math.asin((2 * R) - 1)

def p(x):
	return (math.pi / 40) * math.cos((math.pi / 20) * x)

def funcao_3(x):
	return (2 - ((x ** 2) / 50))

def montecarlo_amostragem_uniforme(x, funcao, xmin, xmax, ymin, ymax):
	S = 0
	x = [(xi * 20) - 10 for xi in x]
	y = [aleatorio() * 2 for i in range(int(1e5))]

	pares = [(x[i], y[i]) for i in range(int(1e5))]

	for par in pares:
		if par[0] >= xmin and par[0] <= xmax:
			if par[1] < funcao(par[0]):
				S += 1

	return (S / len(y)) * ((xmax - xmin) * (ymax - ymin))

def montecarlo_amostragem_simples(x, funcao, xmin, xmax):
	x = [(xi * 20) - 10 for xi in x]
	fx = [funcao(xi) for xi in x]
	med = media(fx)
	desvio = desvpad(fx)
	return [(xmax - xmin) * med, desvio]

def montecarlo_amostragem_importancia(x, funcao, prob, xmin, xmax):
	fxpx = [funcao(xi)/prob(xi) for xi in x]
	med = media(fxpx)
	desvio = desvpad(fxpx)
	return [med, desvio]

def main():
	x = [aleatorio() for i in range(int(1e5))]
	print(f"1.a) {media(x)}")
	print(f"1.b) {desvpad(x)}")

	print(f"2.a) {math.pi/40}")
	print(f"2.b) {distribuicao_(0.6)}")

	x2 = [distribuicao_(R) for R in x]

	print(f"2.c) {media(x2)}")

	print(f"3.a) {80/3}")
	print(f"3.b)i) {montecarlo_amostragem_uniforme(x, funcao_3,  -10, 10, 0, 2)}")

	mcs = montecarlo_amostragem_simples(x, funcao_3,  -10, 10)
	print(f"3.b)i) {mcs[0]} ± {mcs[1]}")

	mci = montecarlo_amostragem_importancia(x2, funcao_3, p, -10, 10)
	print(f"3.b)iii) {mci[0]} ± {mci[1]}")

	plt.hist(x2, bins=100, density=True)
	x_ = [i / 10 for i in range(-100, 101)]
	plt.plot(x_, [p(xi) for xi in x_])
	plt.grid(True)
	plt.show()

main()