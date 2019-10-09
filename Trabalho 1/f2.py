import matplotlib.pyplot as plt
import math
import sys

mi = 1.4e4 # Taxa de consumo de combustível [Kg/s]
M = 2.7e6 # Massa total do foguete [Kg]
Mc0 = M * 0.94 # Massa inicial de combustível [Kg] {94% da massa de combustível}
M0 = M - Mc0 # Massa do foguete sem combustível [Kg]
g = 9.8 # aceleração da gravidade [m/s²]
Vc = 2.7e3 # módulo da velocidade do combustível [m/s]
Vf0 = 0

def massaInstantaneaFoguete(t):
    return M - mi * t

def massaInstantaneaGasExpelido(t):
    return mi * t

def velocidadeAnalitica(t):
    mf = massaInstantaneaFoguete(t)

    return Vf0 - g * t + Vc * math.log(M / mf)

def velocidadeCombustivelExaurido(t):
    return Vf0 - g * t + Vc * math.log(M / M0)

def f(t, m):
    return ((mi * Vc) / m) - g

def momento(t, Vf, Vc_ = Vc):
    return massaInstantaneaFoguete(t) * Vf - massaInstantaneaGasExpelido(t) * Vc_

def euler(h, t_max, f):
    Vf = Vf0

    l_vf = [Vf]
    l_t = [0.]
    l_m = [momento(0, Vf)]

    i = 0
    mf = M
    while mf > M0:
        i += 1
        t = float(i * h)

        mf = massaInstantaneaFoguete(t)

        Vf = Vf + f(t, mf) * h

        l_vf.append(Vf)
        l_t.append(t)
        l_m.append(momento(t, Vf, 0))


    return {
        'Vf': l_vf,
        't': l_t,
        'm': l_m,
    }

def rk2(h, t_max, f):
    Vf = Vf0

    l_vf = [Vf]
    l_t = [0.]
    l_m = [momento(0, Vf)]

    i = 0
    mf = M
    while mf > M0:
        i += 1
        t = float(i * h)

        mf = massaInstantaneaFoguete(t)

        k1 = f(t, mf)
        k2 = f(t + (h / 2), mf + k1 * (h / 2))
        Vf = Vf + k2 * h

        l_vf.append(Vf)
        l_t.append(t)
        l_m.append(momento(t, Vf, 0))


    return {
        'Vf': l_vf,
        't': l_t,
        'm': l_m,
    }

def rk4(h, t_max, f):
    Vf = Vf0

    l_vf = [Vf]
    l_t = [0.]
    l_m = [momento(0, Vf)]

    i = 0
    mf = M
    while mf > M0:
        i += 1
        t = float(i * h)

        mf = massaInstantaneaFoguete(t)

        k1 = f(t, mf)
        k2 = f(t + (h / 2), mf + k1 * (h / 2))
        k3 = f(t + (h / 2), mf + k2 * (h / 2))
        k4 = f(t + h, mf + k3 * h)
        Vf = Vf + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

        l_vf.append(Vf)
        l_t.append(t)
        l_m.append(momento(t, Vf, 0))


    return {
        'Vf': l_vf,
        't': l_t,
        'm': l_m,
    }

def main():
    h = 0.1
    t_max = 200
    e = euler(h, t_max, f)
    r2 = rk2(h, t_max, f)
    r4 = rk4(h, t_max, f)

    plt.plot(e['t'], e['Vf'])
    plt.plot(r2['t'], r2['Vf'])
    plt.plot(r4['t'], r4['Vf'])
    plt.plot(e['t'], [velocidadeAnalitica(t) for t in e['t']])

    plt.legend(['Euler', 'RK2', 'RK4', 'Analitico'])

    plt.show()

    plt.plot(e['t'], e['m'])
    plt.plot(r2['t'], r2['m'])
    plt.plot(r4['t'], r4['m'])
    plt.legend(['Euler', 'RK2', 'RK4'])

    plt.show()

main()