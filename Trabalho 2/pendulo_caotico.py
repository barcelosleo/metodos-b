import matplotlib.pyplot as plt
import math
import numpy as np
import sys

c = 0.05
omega = 0.7
h = 0.01

def f(t, F, V, X):
    return (F * math.cos(omega * t)) - (c * V) - math.sin(X)

def rk4(X_0, V_0, h, F, integration_t, t_max, f):
    X = X_0
    V = V_0

    i = 0
    t = 0

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

    print((X, V))

    dados = {
        't': [t],
        'x': [X],
        'v': [V],
    }

    i = 0

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
    X_0 = 1
    V_0 = 0
    t_max = 200 * math.pi
    integration_t = 800

    for i in range(4, 11):
        F = i / 10

        dados = rk4(X_0, V_0, h, F, integration_t, t_max, f)

        plt.subplot(1, 2, 1)
        plt.plot(dados['t'], dados['v'])
        plt.grid(True)
        plt.title(f"F = {F}")

        plt.subplot(1, 2, 2)
        plt.plot(dados['x'], dados['v'], '.')
        plt.xlim(-math.pi, math.pi)
        plt.grid(True)
        plt.title(f"F = {F}")

        plt.show()

main()