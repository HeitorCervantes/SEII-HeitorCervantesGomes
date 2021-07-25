import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([3,5,7,8])
a2 = np.zeros(10)
a3 = np.ones(10)
a4 = np.random.random(10)
a5 = np.random.randn(1o)
a6 = np.linspace(0,10,100)
a7 = np.arange(0,10,0.02)

a8 = 2*np.random.randn(10000) + 10

np.mean(a1)

np.std(a1)

np.percentile(a1, 80)

x  = np.linspace(1,10,100)
y = 1/x**2 + np.sin(x)

plt.plot(x,y)

dydx = np.gradient(y, x)

plt.plot(x, dydx)

y_int = np.cumsum(y) * (x[1] - x[0])

np.cumsum(np.array([1,2,3,4]))

plt.plot(x, y_int)


