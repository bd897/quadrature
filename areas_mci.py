from scipy import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import time

a = 0
b = np.pi
N = 1000
integral = 0.0
x = np.zeros(N)
y = np.zeros(N)
dx = (b-a)/N

def func( x ):
    return np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111)

# Set Labels
plt.title("MCI")
plt.xlabel("X")
plt.ylabel("Y")

for i in range(N):
    x[i] = random.uniform(a,b)
    y[i] = func( x[i] )
    
    ax.add_patch(Rectangle( (x[i], 0), dx, y[i], linewidth=.5,color='blue',fill=False ))
    integral += y[i]

plt.scatter(x,y, color='red', s=5)
plt.show()
ans = dx * integral
print("Final Integral: ",ans);
