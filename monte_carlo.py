from random import random
import numpy as np

# Визначте функцію, яку потрібно інтегрувати, наприклад, f(x) = x^2
def func(x):
    return x**2

# Визначте межі інтегрування, наприклад, від 0 до 1
a = 0  # нижня межа
b = 2  # верхня межа

# Визначте межі прямокутника по шкалі У, наприклад, від 0 до 4

y_min = 0
y_max = 4

def monte_carlo_integrate(func, a, b, y_min, y_max, num_points):
    x = np.random.uniform(a, b, num_points)
    y = np.random.uniform(y_min, y_max, num_points)
    under_curve = np.sum(y < func(x))
    area = (b - a) * (y_max - y_min) * (under_curve / num_points)
    return area


mc_result = monte_carlo_integrate(func, a, b, y_min, y_max, 1000000) 
print(mc_result)