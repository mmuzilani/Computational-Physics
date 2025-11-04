#!/usr/bin/env python3
"""
Runge-Kutta 2nd Order (RK2) Method with Step-by-Step Output
Author: Md. Mahiuddin Zilani

"""

import numpy as np
import matplotlib.pyplot as plt


def f(t, y):
    return -2 * y  # Example ODE: dy/dt = -2y


def y_exact(t):
    return np.exp(-2 * t)


def rk2_method(f, t0, y0, h, t_end):
    n_steps = int((t_end - t0) / h)
    t_values = np.zeros(n_steps + 1)
    y_values = np.zeros(n_steps + 1)

    # Initial conditions
    t_values[0] = t0
    y_values[0] = y0

    for i in range(n_steps):
        k1 = f(t_values[i], y_values[i])
        k2 = f(t_values[i] + h, y_values[i] + h * k1)
        y_values[i + 1] = y_values[i] + (h / 2) * (k1 + k2)
        t_values[i + 1] = t_values[i] + h

    return t_values, y_values


t0 = 0.0
y0 = 1.0
h = 0.25
t_end = 3.0

# Compute RK2 solution
t_rk2, y_rk2 = rk2_method(f, t0, y0, h, t_end)

# Exact solution
y_true = y_exact(t_rk2)


print("--------------------------------------------------------------")
print(" Step |   t_n   |     y_n (RK2)    |   y_exact    |    Error")
print("--------------------------------------------------------------")
for i in range(len(t_rk2)):
    error = abs(y_true[i] - y_rk2[i])
    print(f"{i:5d} | {t_rk2[i]:7.3f} | {y_rk2[i]:14.6f} | {y_true[i]:11.6f} | {error:10.6f}")
print("--------------------------------------------------------------")


plt.figure(figsize=(8,5))
plt.plot(t_rk2, y_rk2, 'bo-', label="RK2 Approximation")
plt.plot(t_rk2, y_true, 'r--', label="Exact Solution")
plt.title("Runge–Kutta 2nd Order (RK2) Method for dy/dt = -2y")
plt.xlabel("Time t")
plt.ylabel("y(t)")
plt.legend()
plt.grid(True)
plt.show()
