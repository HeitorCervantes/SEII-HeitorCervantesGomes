import numpy as np
import matplotlib.pyplot as plt

N = 10000

x = np.linspace(0,10, N+1)
y= np.exp(-x/10)*np.sin(x)

plt.plot(x,y)

np.mean(y[(x>=4)*(x<=7)])

np.std(y[(x>=4)*(x<=7)])

plt.plot(x, np.gradient(y,x))

dydx = np.gradient(y,x)

x[1:][dydx[1:]*dydx[:-1]<0]

sum(nums[(np.arrange(0,10001, 1)%4 != 0) * (np.arrange(0,10001, 1)%7 != 0)])


