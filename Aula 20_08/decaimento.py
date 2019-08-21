import matplotlib.pyplot as plt
import math

# df/dt = -x/tau

dt = 10e-3
tau = 700
x0 = 1e6
t0 = 0

Xanterior = x0

dts = []

N = 0

Ts = []
Xs = []

while N <= 10e4:
	Xn = Xanterior + dt * (-Xanterior/tau)
	Ts.append(N * dt)
	Xs.append(Xn)

	Xanterior = Xn
	N += 1

Exp = [(math.exp(-i/tau) * x0) for i in Ts]

plt.plot(Ts, Xs)
plt.plot(Ts, Exp)
plt.show()