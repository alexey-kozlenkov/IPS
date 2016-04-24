__author__ = 'Alexey'
from math import sin, cos
import numpy as np


def exact_y(t):
    return sin(5 * t)


def approximate_y(t):
    exact = exact_y(t)
    noise = np.random.normal(0, 1)
    # noise = np.random.uniform(-0.1, 0.1)
    return exact + noise


def exact_u(t):
    return 5 * cos(5 * t)


def approximate_u(t, approx_y, alfa):
    return (approximate_y(t + alfa) - approx_y) / alfa


def nu(delta):
    return delta ** 2
