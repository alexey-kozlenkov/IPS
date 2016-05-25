__author__ = 'Alexey'

import numpy as np
from function import exact_y, exact_u, approximate_y_noise, discrepancy, approximate_y_mush
from plotting import plot_pair
from scipy import optimize

a = 0.
b = 3.
N = 200
h = b / N
t = np.linspace(a, b, N + 1)
exact_y_values = [exact_y(x) for x in t]
exact_u_values = [exact_u(x) for x in t]
bnds = tuple((-5, 5) for i in range(len(t)))


def stabilizer(x):
    return sum(x_i ** 2 for x_i in x)


def prepare_constraints(disturbed_values):
    return {'type': 'eq', 'fun': lambda z: discrepancy(z, disturbed_values, h) - delta}


print 'White noise:'
for sigma in (0.7, 0.5, 0.2, 0.1, 0.01):
    print '\tSolving for sigma={:.3f}'.format(sigma)
    delta = 0.25 * sigma ** 0.5

    disturbed_y_values = [approximate_y_noise(x, sigma) for x in t]

    cons = prepare_constraints(disturbed_y_values)
    z0 = disturbed_y_values
    res = optimize.minimize(stabilizer, z0, method='SLSQP', bounds=bnds, constraints=cons, tol=1e-6)
    approximate_solution = res.x

    plot_pair(t, exact_y_values, disturbed_y_values, 'white_noise/y_values_{:.3f}'.format(sigma),
              2.5, title='Disturbed y (sigma={:.3f})'.format(sigma), color1='forestgreen', color2='coral',
              label1='exact y', label2='disturbed y')

    plot_pair(t, approximate_solution, exact_u_values, 'white_noise/u_values_{:.3f}'.format(sigma), 8,
              title='Approximate solution for sigma={:.3f}'.format(sigma), color1='steelblue', color2='darkorange',
              label1='approximate sol.', label2='exact sol.')

print 'Mush'

w = (50, 70, 100)
for a, delta in (((0.1, 0.09, 0.11), 0.3), ((0.05, 0.05, 0.05), 0.15), ((0.025, 0.025, 0.025), 0.075)):
    print '\tSolving for delta={:.3f}'.format(delta)
    disturbed_y_values = [approximate_y_mush(x, a, w) for x in t]
    cons = prepare_constraints(disturbed_y_values)

    z0 = disturbed_y_values
    res = optimize.minimize(stabilizer, z0, method='SLSQP', bounds=bnds, constraints=cons, tol=1e-6)
    approximate_solution = res.x

    plot_pair(t, exact_y_values, disturbed_y_values, 'mush/y_values_{:.3f}'.format(delta), 2.5,
              title='Disturbed y (delta={:.3f})'.format(delta), color1='forestgreen', color2='coral', label1='exact y',
              label2='disturbed y')

    plot_pair(t, approximate_solution, exact_u_values, 'mush/u_values_{:.3f}'.format(delta), 8,
              title='Approximate solution for delta={:.3f}', color1='steelblue', color2='darkorange',
              label1='approximate sol.', label2='exact sol.')
