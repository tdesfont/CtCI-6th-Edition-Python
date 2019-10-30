import matplotlib.pyplot as plt
import numpy as np
import random
from math import sin, cos

square = {"x": np.array([1, 0, 0, 1, 1]),
          "y": np.array([0, 0, 1, 1, 0])}

N = 40
P = 30

A = np.array([[cos(i/5)*cos(j/5) for i in range(N)] for j in range(N)])
mask = A > 0.6
off = -0.5

fig = plt.figure(figsize=(N, N))
plt.title('Easter egg.')
plt.imshow(A*mask, cmap='Blues')
for i in np.linspace(0, N, N):
    plt.plot(i*np.ones(N)+off, np.linspace(0, N, N)+off, alpha=0.4, color="k")
for i in np.linspace(0, N, N):
    plt.plot(np.linspace(0, N, N)+off, i*np.ones(N)+off, alpha=0.4, color="k")
for c in ['red', 'purple', 'green', 'gray']:
    plt.scatter(np.random.random(P)*N, np.random.random(P)*N, c=c, edgecolor="k", alpha=0.7, s=random.random()*30+40)
plt.colorbar()
plt.show()
