import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**4 + x**2 - 4*x - 4

x = np.linspace(-3,3,600)
plt.plot(x,f(x))
plt.axhline(0)
plt.show()
