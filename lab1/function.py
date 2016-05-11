__author__ = 'Alexey'
from math import sin, cos
import numpy as np


def exact_y(t):
    return sin(5 * t)


def approximate_y_noise(t, sigma2):
    exact = exact_y(t)
    noise = np.random.normal(0, sigma2)
    return exact + noise


def approximate_y_mush(t):
    pass

def exact_u(t):
    return 5 * cos(5 * t)


def approximate_u(t, approx_y, alfa):
    return (approx_y[up_round(t + alfa, sorted(approx_y.keys()))] - approx_y[down_round(t - alfa, sorted(approx_y.keys()))]) / (2* alfa)


def eta(delta):
    return 10 * delta ** 0.5


def up_round(x, values):
    values = list(reversed(values))
    for right, left in zip(values[:-1], values[1:]):
        if left <= x <= right:
            return right

def down_round(x, values):
    values = list(reversed(values))
    for right, left in zip(values[:-1], values[1:]):
        if left <= x <= right:
            return left
