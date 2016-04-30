__author__ = 'Alexey'
from function import *
from matplotlib import pyplot as plot
from plotting import plot_pair

dispersion2 = 0.1
delta = 3 * dispersion2 ** 0.5
alfa = delta / eta(delta)
print 'delta = {}'.format(delta)
print 'alfa = {}'.format(alfa)

t = np.linspace(0, 3, 1000 + 1)
t_big = np.linspace(0, 9, 3000 + 1)
exact_y_values = [exact_y(x) for x in t]
approximate_y_values_all = {x: approximate_y(x, dispersion2) for x in t_big}
approximate_y_values = [approximate_y_values_all[x] for x in t]

plot_pair(t, approximate_y_values, exact_y_values, 'y values', 'y(t)', label1='approximate', label2='exact')

exact_solution = [exact_u(x) for x in t]
approximate_solution = [approximate_u(x, approximate_y_values_all, alfa) for x in t]

plot_pair(t, approximate_solution, exact_solution, 'u values', 'u(t)', label1='approximate', label2='exact')
