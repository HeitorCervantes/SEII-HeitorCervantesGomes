import numpy as np
import matplotlib.pyplot as plt

A = np.array([[3,2,1],[5,-5,4],[6,0,1]])
c = np.array([4,3,0])

np.linalg.solve(A,c)
