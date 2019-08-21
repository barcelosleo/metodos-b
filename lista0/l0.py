import matplotlib.pyplot as plt
import math

def fatorial(n):
    if n == 0 or n == 1:
        return 1

    fat = 1
    for i in range(n, 1, -1):
        fat *= i

    return fat

def somatorio(n):
    soma = 0
    for i in range(n, 1, -1):
        soma += i

    return soma

def sen_maclaurin(x, N = 1):
    seno = 0
    n = 0
    while n <= N:
        parcela = ((-1) ** n) * (x ** (2 * n + 1)) / fatorial(2 * n + 1)
        seno += parcela
        n += 1

    return seno

def cos_maclaurin(x, N = 1):
    cos = 0
    n = 0
    while n <= N:
        parcela = ((-1) ** n) * (x ** (2 * n)) / fatorial(2 * n)
        cos += parcela
        n += 1

    return cos

def ex_2():
    n = int(input("Digite um valor para o cálculo do fatorial:\n"))
    print(f"n = {n}\nn! = {fatorial(n)}\nSomatorio = {somatorio(n)}")

def ex_3():
    x = []
    for i in range(100):
        i_ = (i * 2 * math.pi) / 100
        x.append(i_)

    y_sen = [math.sin(i) for i in x]
    y_sen_m1 = [sen_maclaurin(i, 1) for i in x]
    y_sen_m3 = [sen_maclaurin(i, 3) for i in x]
    y_sen_m5 = [sen_maclaurin(i, 5) for i in x]
    y_sen_m7 = [sen_maclaurin(i, 7) for i in x]

    plt.plot(x, y_sen)
    plt.plot(x, y_sen_m1)
    plt.plot(x, y_sen_m3)
    plt.plot(x, y_sen_m5)
    plt.plot(x, y_sen_m7)

    plt.xlabel('x valores de 0 a 2pi')

    plt.legend(['y = sen', 'y = sen_maclaurin_m1', 'y = sen_maclaurin_m3', 'y = sen_maclaurin_m5', 'y = sen_maclaurin_m7'], loc='upper left')
    plt.show()

def ex_4():
    ref = math.sin(math.pi)
    p = int(input("Digite uma precisão:\n"))
    N = 0
    ordens = []
    erros = []
    while True:
        sen_m = sen_maclaurin(math.pi, N)
        erro = abs(sen_m - ref)
        ordens.append(N)
        erros.append(erro)
        if erro <= 10 ** -p:
            break
        N += 1
    print(f"Ordem aproximada para precisão de {p} casas decimais: {N}")
    plt.plot(ordens, erros)
    plt.xlabel(r"N")
    plt.yscale('log')
    plt.ylabel(r"$\epsilon$")
    plt.show()

ex_3()