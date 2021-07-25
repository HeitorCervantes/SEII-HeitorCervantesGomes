import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([3,5,7,8])
a2 = np.zeros(10)
a3 = np.ones(10)
a4 = np.random.random(10)
a5 = np.random.randn(1o)
a6 = np.linspace(0,10,100)
a7 = np.arange(0,10,0.02)

print(a1[:-2])

names = np.array(['pete', 'jonh', 'Heitor'])

f = lambda s: s[0]

first_letter = np.vectoriza(lambda s: s[0])(names)=='j'

