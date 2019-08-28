import matplotlib.pyplot as plt
import math

# df/dt = -x/tau

dt = 10e-3
tau = 700
x0 = 1e6
t0 = 0

Xn = x0

dts = []

N = 0

Ts = []
Xs = []

T = 0

while T <= 2500:
	Xn1 = Xn + dt * (-Xn/tau)
	T = N * dt
	Ts.append(T)
	Xs.append(Xn1)

	Xn = Xn1
	N += 1

Exp = [(math.exp(-i/tau) * x0) for i in Ts]

plt.plot(Ts, Xs)
plt.plot(Ts, Exp)
plt.show()