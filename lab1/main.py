__author__ = 'Alexey'
from lab1.function import *
from lab1.plotting import plot_pair

t = np.around(np.linspace(0, 3, 1000 + 1), 8)
t_big = np.around(np.linspace(-1.5, 4.5, 2000 + 1), 8)
exact_y_values = [exact_y(x) for x in t]
exact_solution = [exact_u(x) for x in t]

print 'White noise:'
for dispersion2 in (0.7, 0.4, 0.1, 0.05):
    print '\tdispersion^2 = {}'.format(dispersion2)
    delta = 3 * dispersion2 ** 0.5
    alfa = delta / eta(delta)
    print '\t\tdelta = {}'.format(delta)
    print '\t\talfa = {}'.format(alfa)

    approximate_y_values_all = {x: approximate_y_noise(x, dispersion2) for x in t_big}
    approximate_y_values = [approximate_y_values_all[x] for x in t]

    plot_pair(t, approximate_y_values, exact_y_values, 'white_noise\y_values_{}'.format(dispersion2), 5,
              'y(t). dispersion = {}'.format(dispersion2), label1='approximate', label2='exact')

    approximate_solution = [approximate_u(x, approximate_y_values_all, alfa) for x in t]

    plot_pair(t, approximate_solution, exact_solution, 'white_noise\u_values_{}'.format(dispersion2), 15,
              'u(t). dispersion = {}'.format(dispersion2), label1='approximate', label2='exact')

print 'Mush:'

w = (50, 70, 100)
for a, delta in (((0.1, 0.09, 0.11), 0.3), ((0.05, 0.05, 0.05), 0.15), ((0.025, 0.025, 0.025), 0.075)):
    print '\ta = {}'.format(a)
    print '\tdelta = {}'.format(delta)
    alfa = delta / eta(delta)
    print '\talfa = {}'.format(alfa)

    approximate_y_values_all = {x: approximate_y_mush(x, a, w) for x in t_big}
    approximate_y_values = [approximate_y_values_all[x] for x in t]

    plot_pair(t, approximate_y_values, exact_y_values, 'mush\y_values_{}'.format(delta), 5,
              'y(t). delta = {}, a = {}'.format(delta, a), label1='approximate', label2='exact')

    approximate_solution = [approximate_u(x, approximate_y_values_all, alfa) for x in t]

    plot_pair(t, approximate_solution, exact_solution, 'mush\u_values_{}'.format(delta), 15,
              'u(t). delta = {}, a = {}'.format(delta, a), label1='approximate', label2='exact')