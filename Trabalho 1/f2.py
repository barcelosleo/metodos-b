import matplotlib.pyplot as plt
import math
import sys

mi = 1.4e4 # Taxa de consumo de combustível [Kg/s]
M = 2.7e6 # Massa total do foguete [Kg]
Mc0 = M * 0.94 # Massa inicial de combustível [Kg] {94% da massa de combustível}
M0 = M - Mc0 # Massa do foguete sem combustível [Kg]
g = 9.8 # aceleração da gravidade [m/s²]
Vc = 3e3 # módulo da velocidade do combustível [m/s]
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

def momento(t, mf, mc, Vf):
    return (mf * Vf) + (mc * (Vf - Vc))

def energia(m, v, h):
    return ((m * v ** 2) / 2) - (m * g * h)

def euler(h, f):
    Vf = Vf0

    l_vf = [Vf]
    l_t = [0.]
    l_m = [momento(0, M, 0, Vf)]
    l_h = [0]
    l_e = [0]

    i = 0
    t = 0
    mf = M
    while mf > M0:
        i += 1
        t = float(i * h)

        mf = massaInstantaneaFoguete(t)

        Vf = Vf + f(t, mf) * h

        l_vf.append(Vf)
        l_t.append(t)
        l_m.append(momento(t, mf, mi * t, Vf))
        l_h.append(l_h[-1] + (Vf * h))
        l_e.append(energia(mf, Vf, l_h[-1]))


    return {
        'Vf': l_vf,
        't': l_t,
        'm': l_m,
        'h': l_h,
        'e': l_h,
    }

def rk2(h, f):
    Vf = Vf0

    l_vf = [Vf]
    l_t = [0.]
    l_m = [momento(0, M, 0, Vf)]
    l_h = [0]
    l_e = [0]

    i = 0
    t = 0
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
        l_m.append(momento(t, mf, mi * t, Vf))
        l_h.append(l_h[-1] + (Vf * h))
        l_e.append(energia(mf, Vf, l_h[-1]))


    return {
        'Vf': l_vf,
        't': l_t,
        'm': l_m,
        'h': l_h,
        'e': l_h,
    }

def rk4(h, f):
    Vf = Vf0

    l_vf = [Vf]
    l_t = [0.]
    l_m = [momento(0, M, 0, Vf)]
    l_h = [0]
    l_e = [0]

    i = 0
    t = 0
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
        l_m.append(momento(t, mf, mi * t, Vf))
        l_h.append(l_h[-1] + (Vf * h))
        l_e.append(energia(mf, Vf, l_h[-1]))


    return {
        'Vf': l_vf,
        't': l_t,
        'm': l_m,
        'h': l_h,
        'e': l_e,
    }

def main():
    h = 0.001
    e = euler(h, f)
    r2 = rk2(h, f)
    r4 = rk4(h, f)

    analitico = {
        't': e['t'],
        'Vf': [velocidadeAnalitica(t) for t in e['t']]
    }

    plt.subplot(1, 2, 1)
    plt.plot(e['t'], e['Vf'])
    plt.plot(r2['t'], r2['Vf'])
    plt.plot(r4['t'], r4['Vf'])
    plt.plot(analitico['t'], analitico['Vf'])
    plt.ylabel('V(m/s)')
    plt.xlabel('t(s)')

    plt.subplot(1, 2, 2)
    plt.plot(e['t'], e['h'])
    plt.plot(r2['t'], r2['h'])
    plt.plot(r4['t'], r4['h'])
    plt.ylabel('Altura(m)')
    plt.xlabel('t(s)')

    plt.legend(['Euler', 'RK2', 'RK4'])

    plt.show()

    p = 4

    valor_analitico = velocidadeAnalitica(e['t'][-1])

    legends = []

    l_h = []
    l_e_e = []
    l_e_r2 = []
    l_e_r4 = []

    for j in range(p):
        h = 1 * 10 ** -j

        e = euler(h, f)
        r2 = rk2(h, f)
        r4 = rk4(h, f)

        l_h.append(h)

        l_e_e.append(abs(valor_analitico - e['Vf'][-1]))
        l_e_r2.append(abs(valor_analitico - r2['Vf'][-1]))
        l_e_r4.append(abs(valor_analitico - r4['Vf'][-1]))

    plt.plot(l_h, l_e_e, '.-')
    plt.plot(l_h, l_e_r2, '.-')
    plt.plot(l_h, l_e_r4, '.-')
    plt.legend(['Euler', 'RK2', 'RK4'])
    plt.title('Erros')

    plt.ylabel(r'$ |V(' + str(e['t'][-1]) + ') - V_{analitico}(' + str(e['t'][-1]) +')| $')
    plt.xlabel('h')

    plt.xscale('log')
    plt.yscale('log')

    plt.show()


    for j in range(1, p):
        h = 1 * 10 ** -j

        e = euler(h, f)
        r2 = rk2(h, f)
        r4 = rk4(h, f)

        erro_e = []
        erro_r2 = []
        erro_r4 = []

        legends.append(f'Euler h = {1 * 10 ** -j}')
        legends.append(f'RK2 h = {1 * 10 ** -j}')
        legends.append(f'RK4 h = {1 * 10 ** -j}')

        for i in range(len(e['Vf'])):
            erro_e.append(abs(e['Vf'][i] - analitico['Vf'][i]))
            erro_r2.append(abs(r2['Vf'][i] - analitico['Vf'][i]))
            erro_r4.append(abs(r4['Vf'][i] - analitico['Vf'][i]))

        plt.plot(e['t'], erro_e)
        plt.plot(e['t'], erro_r2)
        plt.plot(e['t'], erro_r4)


    plt.legend(legends)
    plt.yscale('log')
    plt.ylabel(r'$ | V_n - V_{analitico} | $')
    plt.xlabel('h')
    plt.title('Erros')

    plt.show()

main()