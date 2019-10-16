import matplotlib.pyplot as plt
import math
import numpy as np
import sys
import time

c = 0.05
omega = 0.7
h = 0.01

def f_(t, F, V, X):
    return (F * math.cos(omega * t)) - (c * V) - math.sin(X)

def rk4(X_0, V_0, h, F, integration_t, t_max, isPC = False):
    X = X_0
    V = V_0

    i = 0
    t = 0
    f = lambda t, F, V, X: (F * math.cos(omega * t)) - (c * V) - math.sin(X)

    while t <= integration_t:
        k1_X = V
        k1_V = f(t, F, V, X)

        k2_X = V + (h / 2) * k1_V
        k2_V = f(t + (h / 2), F, V + k1_V * (h / 2), X + k1_X * (h / 2))

        k3_X = V + (h / 2) * k2_V
        k3_V = f(t + (h / 2), F, V + k2_V * (h / 2), X + k2_V * (h / 2))

        k4_X = V +  h * k3_V
        k4_V = f(t + h, F, V + k3_V * h, X + k3_X * h)

        i += 1
        t = i * h

        X = X + (h / 6) * (k1_X + 2 * k2_X + 2 * k3_X + k4_X)
        V = V + (h / 6) * (k1_V + 2 * k2_V + 2 * k3_V + k4_V)

        if X > math.pi:
            X -= 2 * math.pi
        elif X <= -math.pi:
            X += 2 * math.pi

    dados = {
        't': [t],
        'x': [X],
        'v': [V],
    }

    i = 0
    if isPC:
        pc = 1
        while t <= (integration_t + t_max):
            k1_X = V
            k1_V = f(t, F, V, X)

            k2_X = V + (h / 2) * k1_V
            k2_V = f(t + (h / 2), F, V + k1_V * (h / 2), X + k1_X * (h / 2))

            k3_X = V + (h / 2) * k2_V
            k3_V = f(t + (h / 2), F, V + k2_V * (h / 2), X + k2_V * (h / 2))

            k4_X = V +  h * k3_V
            k4_V = f(t + h, F, V + k3_V * h, X + k3_X * h)

            X = X + (h / 6) * (k1_X + 2 * k2_X + 2 * k3_X + k4_X)
            V = V + (h / 6) * (k1_V + 2 * k2_V + 2 * k3_V + k4_V)

            i += 1
            t = integration_t +  i * h

            if X > math.pi:
                X -= 2 * math.pi
            elif X <= -math.pi:
                X += 2 * math.pi

            if abs((t - integration_t) - ((2 * math.pi) / omega) * pc) < 6e-3:
                dados['t'].append(t)
                dados['x'].append(X)
                dados['v'].append(V)
                pc += 1
    else:
        while t <= (integration_t + t_max):
            k1_X = V
            k1_V = f(t, F, V, X)

            k2_X = V + (h / 2) * k1_V
            k2_V = f(t + (h / 2), F, V + k1_V * (h / 2), X + k1_X * (h / 2))

            k3_X = V + (h / 2) * k2_V
            k3_V = f(t + (h / 2), F, V + k2_V * (h / 2), X + k2_V * (h / 2))

            k4_X = V +  h * k3_V
            k4_V = f(t + h, F, V + k3_V * h, X + k3_X * h)

            X = X + (h / 6) * (k1_X + 2 * k2_X + 2 * k3_X + k4_X)
            V = V + (h / 6) * (k1_V + 2 * k2_V + 2 * k3_V + k4_V)

            i += 1
            t = integration_t +  i * h

            if X > math.pi:
                X -= 2 * math.pi
            elif X <= -math.pi:
                X += 2 * math.pi

            dados['t'].append(t)
            dados['x'].append(X)
            dados['v'].append(V)

    return dados

def main():
    t_0 = time.time()
    X_0 = 1
    V_0 = 0
    t_max = 20 * math.pi
    integration_t = 800

    for i in range(0, 11):
        F = i / 10

        print(f"Iniciando processamento para F = {F}")
        t_i = time.time()
        dados = rk4(X_0, V_0, h, F, integration_t, t_max)
        phase = rk4(X_0, V_0, h, F, integration_t, t_max * 60)
        poincare = rk4(X_0, V_0, h, F, integration_t, t_max * 500, isPC=True)
        t_f = time.time() - t_i
        tempo = time.strftime("%H:%M:%S", time.gmtime(t_f))
        print(f"Finalizado processamento em {tempo}\n")

        plt.subplot(1, 3, 1)
        plt.plot([t - integration_t for t in dados['t']], dados['v'])
        plt.xticks([0, 10 * math.pi, 20 * math.pi], ["$0$", "$10\pi$", "$20\pi$"])
        plt.ylim(-4, 4)
        plt.xlim(0, t_max)
        plt.grid(True)
        plt.ylabel("$v$")
        plt.xlabel("$t'$")
        plt.title(f"F = {F}")

        plt.subplot(1, 3, 2)
        plt.plot(phase['x'], phase['v'], '.')
        plt.xticks([-math.pi, 0, math.pi], ["$-\pi$", "$0$", "$\pi$"])
        plt.xlim(-math.pi, math.pi)
        plt.ylim(-4, 4)
        plt.grid(True)
        plt.xlabel("$x$")
        plt.title(f"F = {F}")

        plt.subplot(1, 3, 3)
        plt.plot(poincare['x'], poincare['v'], '.')
        plt.xticks([-math.pi, 0, math.pi], ["$-\pi$", "$0$", "$\pi$"])
        plt.xlim(-math.pi, math.pi)
        plt.ylim(-4, 4)
        plt.grid(True)
        plt.xlabel("$x$")
        plt.title(f"F = {F}")

        plt.savefig(f"ignore.{time.time()}_F_{F}.png")
        plt.close()

    t_f = time.time() - t_0
    tempo = time.strftime("%H:%M:%S", time.gmtime(t_f))
    print(f"\nTempo total de Processamento {tempo}\n")

main()