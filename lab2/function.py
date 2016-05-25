__author__ = 'Alexey'
from math import sin, cos
import numpy as np


def exact_y(t):
    return sin(5 * t)


def approximate_y_noise(t, sigma2):
    exact = exact_y(t)
    noise = np.random.normal(0, sigma2)
    return exact + noise


def approximate_y_mush(t, a, w):
    exact = exact_y(t)
    mush = sum(a[i] * sin(w[i] * t) for i in range(len(a)))
    return exact + mush


def exact_u(t):
    return 5 * cos(5 * t)


def discrepancy(approximate_solution, apprpximate_right_part, dt):
    result = 0.
    n = len(apprpximate_right_part)
    for i in range(n):
        result += dt * (dt * sum(approximate_solution[:i + 1]) - apprpximate_right_part[i]) ** 2
    return result
