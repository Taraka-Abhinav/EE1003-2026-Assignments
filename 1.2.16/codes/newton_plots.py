import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**4 + x**2 - 4*x - 4

def df(x):
    return 4*x**3 + 2*x - 4

x0 = 2
x1 = x0 - f(x0)/df(x0)
root = 1.6762517

plt.style.use('dark_background')

# Plot 1
fig1, ax1 = plt.subplots()
x = np.linspace(0,3,400)
ax1.plot(x,f(x))
tangent = f(x0)+df(x0)*(x-x0)
ax1.plot(x,tangent,'--')
ax1.scatter(x0,f(x0))
ax1.scatter(x1,0)
ax1.axhline(0)
plt.show()

# Plot 2 (zoom)
fig2, ax2 = plt.subplots()
x_zoom = np.linspace(1.4,2.1,400)
ax2.plot(x_zoom,f(x_zoom))
ax2.axhline(0)
ax2.scatter(x1,0)
plt.show()

# Plot 3 full
fig3, ax3 = plt.subplots()
x_full = np.linspace(-3,3,600)
ax3.plot(x_full,f(x_full))
ax3.axhline(0)
ax3.axvline(0)
ax3.scatter(root,0)
plt.show()
