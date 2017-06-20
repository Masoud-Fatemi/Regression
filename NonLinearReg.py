import matplotlib.pylab as plt
import numpy as np
from scipy.optimize import curve_fit
import help
import random
random.seed(5)

data_adr = 'data'
x, y = help.load(data_adr); del data_adr
x_new = np.linspace(np.min(x), np.max(x), 50)

param_linear = curve_fit(help.linear, x, y)
[a, b] = param_linear[0]
y_linear = help.linear(x_new, a, b)
print "\n"
print "Linear Regression"
print "y = ax + b"
print "a = %0.5f   b = %0.5f" %(a, b)

param_quadratic = curve_fit(help.quadratic, x, y)
[a, b, c] = param_quadratic[0]
y_quadratic = help.quadratic(x_new, a, b, c)
print "\n"
print "Quadratic Regression"
print "y = ax^2 + bx + c"
print "a = %0.5f   b = %0.5f   c = %0.5f" %(a, b, c)

param_cube = curve_fit(help.cube, x, y)
[a, b, c, d] = param_cube[0]
y_cube = help.cube(x_new, a, b, c, d)
print "\n"
print "Cube Regression"
print "y = ax^3 + bx^2 + cx + d"
print "a = %0.5f   b = %0.5f   c = %0.5f   d = %0.5f" %(a, b, c, d)

plt.close()
plt.figure('Non-Linear Regression')
plt.xlabel('Powder factor/Primary relative density')
plt.ylabel('Percent sitting')
plt.plot(x, y, 'mo', label='Data points')
plt.plot(x_new, y_linear, 'k-', label= 'Linear Regression')
plt.plot(x_new, y_quadratic, 'b--', label= 'Quadratic Regression')
plt.plot(x_new, y_cube, 'r-', label= 'Cube Regression')
plt.plot()
plt.grid()
plt.legend()
plt.show()