import numpy as np

def sincos(x, a,b):
  return a*np.cos(b*x) + b*np.sin(a*x)

def gaussian(x, amp, cen, wid):
    return amp * np.exp(-(x-cen)**2 /wid)

def linear(x, a, b):
    return a*x + b

def quadratic(x, a, b, c):
    return a*(x**2) + b*x + c

def cube(x, a, b, c, d):
    return a*(x**3) + b*(x**2) + c*x + d

    
def load(file):
    data = open(file,'r').read().split('\n')
    data = [i for i in data if i.rstrip()]
    x, y = [], []
    for line in data:
        x.append(float(line.split(' ')[0]))
        y.append(float(line.split(' ')[1]))
    x = np.asarray(x)
    y = np.asarray(y)
    return x, y