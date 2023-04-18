from scipy import random
import numpy as np
import matplotlib.pyplot as plt

a = 0
b = np.pi
N = 10000
areas = []

def func( x ):
    return np.sin(x)

for i in range(N):
    xrand = np.zeros(N)
    integral = 0.0
    
    for j in range(len(xrand)):
        xrand[j] = random.uniform(a,b)
        integral += func( xrand[j] )
    
    ans = (b-a)/float(N) * integral
    areas.append(ans)

plt.title("Dristribution of Areas")
plt.hist(areas, bins = 30, ec = 'black')
plt.xlabel("Areas")
plt.show()
