import math

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
	return ((1 / len(dados)) * sum([(xi - med) ** 2 for xi in dados]) ) ** (1 / 2)

def distribuicao_(R):
    return (20 / math.pi) * math.asin((2 * R) - 1)

def main():
	print(distribuicao_(0.6))

main()