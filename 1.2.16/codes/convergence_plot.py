import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**4 + x**2 - 4*x - 4

def df(x):
    return 4*x**3 + 2*x - 4

true_root = 1.676251739196307

x = 2.0
errors = []
iterations = []

for i in range(7):
    errors.append(abs(x - true_root))
    iterations.append(i)
    x = x - f(x)/df(x)

fig, ax = plt.subplots()
ax.plot(iterations, np.log10(errors), marker='o')
ax.grid(True)
plt.show()
