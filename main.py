__author__ = 'Alexey'
from function import *
from matplotlib import pyplot as plot
from plotting import plot_pair

t = np.linspace(0, 3, 1000, endpoint=True)

approx_y_values = [approximate_y(x) for x in t]
exact_y_values = [exact_y(x) for x in t]
delta = max(map(lambda x, y: abs(x - y), approx_y_values, exact_y_values))
print "Delta = {:.5f}".format(delta)

plot_pair(t, approx_y_values, exact_y_values, 'y values', 'y(t)', label1='approximate', label2='exact')

alfa = delta / nu(delta)

approx_solution = [approximate_u(t[i], approx_y_values[i], alfa) for i in range(len(t))]
exact_solution = [exact_u(x) for x in t]
plot_pair(t, approx_solution, exact_solution, 'u values', 'u(t)', label1='approximate', color1='orange', label2='exact')
