from scipy import random
import numpy as np
import matplotlib.pyplot as plt

a = -2
b = 2
n = 100
step = (b-a)/2
h = (a+b)/2


def func( x ):
    return (x+3)*((x-2)**2)*((x+1)**3)


def simpsons(a,b,h):
    fa = func(a)
    fh = func(h)
    fb = func(b)
    print(fa, fh, fb, h)
    
    return (step/3)*(fa + 4*fh + fb)


def simpsons_graph(a,b,h,x):
    fa = func(a)
    fh = func(h)
    fb = func(b)
    p1 = ( (x-h)*(x-b) )/( (a-h)*(a-b) )*fa
    p2 = ( (x-a)*(x-b) )/( (h-a)*(h-b) )*fh
    p3 = ( (x-a)*(x-h) )/( (b-a)*(b-h) )*fb
    
    return (p1 + p2 + p3)

x1 = np.linspace(a,b,n)
y1 = func(x1)

x2 = np.linspace(a,b,n)
y2 = simpsons_graph(a,b,h,x2)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

integral = simpsons(a,b,h)
print("The Integral of f(x) using Simpson's Rule: ", integral)

plt.plot(x1,y1,'b')
plt.plot(x2,y2,'r')
plt.show()

