

def Fg(x):
  return (6.7e-11 * 5.98e24) / ((6.35e6 + x) ** 2)

print(Fg(10000))