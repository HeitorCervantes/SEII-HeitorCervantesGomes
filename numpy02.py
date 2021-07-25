import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([3,5,7,8])
a2 = np.zeros(10)
a3 = np.ones(10)
a4 = np.random.random(10)
a5 = np.random.randn(1o)
a6 = np.linspace(0,10,100)
a7 = np.arange(0,10,0.02)

print(2*a1)
print(1/a1)
print(a1>4)
print(2*a1 + 10 + 1/a1)
print(a6**2)

y = a6**2
plt.plot(a6,y)

plt.hist(a4)

x = a6

def f(x):
	return x**2 * np.sin(x) / np.exp(-x)

y = f(x)

plt.plot(x,y)
