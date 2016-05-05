__author__ = 'Alexey'
from function import *
from plotting import plot_pair

for dispersion2 in (0.7, 0.4, 0.1, 0.05):
    print 'dispersion^2 = {}'.format(dispersion2)
    delta = 3 * dispersion2 ** 0.5
    alfa = delta / eta(delta)
    print '\tdelta = {}'.format(delta)
    print '\talfa = {}'.format(alfa)

    t = np.around(np.linspace(0, 3, 1000 + 1), 8)
    t_big = np.around(np.linspace(-1.5, 4.5, 2000 + 1), 8)
    exact_y_values = [exact_y(x) for x in t]
    approximate_y_values_all = {x: approximate_y(x, dispersion2) for x in t_big}
    approximate_y_values = [approximate_y_values_all[x] for x in t]

    plot_pair(t, approximate_y_values, exact_y_values, 'y_values_{}'.format(dispersion2), 5,
              'y(t). dispersion = {}'.format(dispersion2), label1='approximate', label2='exact')

    exact_solution = [exact_u(x) for x in t]
    approximate_solution = [approximate_u(x, approximate_y_values_all, alfa) for x in t]

    plot_pair(t, approximate_solution, exact_solution, 'u_values_{}'.format(dispersion2), 15,
              'u(t). dispersion = {}'.format(dispersion2), label1='approximate', label2='exact')
