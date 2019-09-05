def euler_explicito(x0, t0, h, tMax, function):
	x = x0
	t = t0
	lista_x = []
	lista_t = []

	while t <= tMax:
		x = x + function(x, t) * h
		t += h

		lista_x.append(x)
		lista_t.append(t)

	return (x, t)

def euler_crommer(v0, x0, t0, h, tMax, function):
	x = x0
	v = v0
	t = t0
	lista_x = []
	lista_t = []

	while t <= tMax:
		v = v + function(x, t, v) * h
		x = x + v * h
		t += h

		lista_x.append(x)
		lista_t.append(t)

	return (x, t)

