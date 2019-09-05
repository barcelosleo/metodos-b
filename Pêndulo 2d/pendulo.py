import matplotlib.pyplot as plt
import math
import time

theta0_x = math.pi/2 # rad angulo com eixo z
theta0_y = math.pi/2 # rad angulo com eixo z
vt0 = 1 # m/s
omega0_x = -0.5 # rad/s
omega0_y = -0.5 # rad/s
g = 10 # m/s
m = 1 # kg
h = 0.01 # s
L = 1 # m
maxT = 20 # s
N = 20
step = (maxT / N)
t = 0
alpha = lambda theta: (-(m * g) / L) * math.sin(theta)

# ------------------------------------------ Velocity-Verlet ------------------------------------------ #

theta_N_x = theta0_x
theta_N_y = theta0_y

omega_N_x = omega0_x
omega_N_y = omega0_y

lista_theta_x_ = [L*math.sin(theta0_x)]
lista_theta_y_ = [L*math.sin(theta0_y)]
lista_theta_x = [theta0_x]
lista_theta_y = [theta0_y]
lista_omega = []
lista_energia = []
lista_tempos = []
cores = [-L*math.cos(theta0_x)*math.cos(theta0_y)]

# plt.ion()
# plt.show()

while t <= maxT:
	alpha_N_x = alpha(theta_N_x)
	alpha_N_y = alpha(theta_N_y)

	theta_N1_x = theta_N_x + omega_N_x * h + (alpha_N_x / 2) * (h ** 2)
	theta_N1_y = theta_N_y + omega_N_y * h + (alpha_N_y / 2) * (h ** 2)

	alpha_N1_x = alpha(theta_N1_x)
	alpha_N1_y = alpha(theta_N1_y)

	omega_N1_x  = omega_N_x + ((alpha_N_x + alpha_N1_x) / 2) * h
	omega_N1_y  = omega_N_y + ((alpha_N_y + alpha_N1_y) / 2) * h

	t += h

	lista_theta_x.append(theta_N1_x)
	lista_theta_y.append(theta_N1_y)
	lista_theta_x_.append(L*math.sin(theta_N1_x))
	lista_theta_y_.append(L*math.sin(theta_N1_y))
	lista_tempos.append(t)
	cores.append(-L*math.cos(theta_N1_y)*math.cos(theta_N1_x))

	theta_N_x = theta_N1_x
	theta_N_y = theta_N1_y

	omega_N_x = omega_N1_x
	omega_N_y = omega_N1_y


plt.subplot(1, 2, 1)
plt.title(f"L = {L}, " + r"$ \theta_{x0} = $" + f"{round(theta0_x, 2)}" + r", $ \theta_{y0} = $" + f"{round(theta0_y, 2)}\n" + r"$ \omega_{x0} = $" + f"{omega0_x}" + r", $ \omega_{y0} = $" + f"{omega0_y}")
plt.plot(lista_theta_x, lista_theta_y)
plt.ylabel(r"$ \theta_{y} $")
plt.xlabel(r"$ \theta_{x} $")
plt.grid(True)

plt.subplot(1, 2, 2)
# plt.title(f"L = {L}, " + r"$ \theta_{x0} = $" + f"{theta0_x}" + r", $ \theta_{y0} = $" + f"{theta0_y}\n" + r"$ \omega_{x0} = $" + f"{omega0_x}" + r", $ \omega_{y0} = $" + f"{omega0_y}")
plt.scatter(
	lista_theta_x_,
	lista_theta_y_,
	marker='.',
	c=cores
)
plt.colorbar()
plt.ylabel("y")
plt.xlabel("x")
plt.grid(True)

	# plt.draw()
	# plt.pause(1e-17)
	# plt.clf()

plt.show()