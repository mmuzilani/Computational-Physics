#!/usr/bin/env python3
"""
Euler Method with Step-by-Step Output
Author: Md. Mahiuddin Zilani

"""

import numpy as np
import matplotlib.pyplot as plt


# Define the ODE dy/dt = f(t, y)

def f(t, y):
    return -2 * y  # Example differential equation

# -----------------------------
# Analytical (exact) solution
# -----------------------------
def y_exact(t):
    return np.exp(-2 * t)

# -----------------------------
# Euler Method Implementation
# -----------------------------
def euler_method(f, t0, y0, h, t_end):
    n_steps = int((t_end - t0) / h)
    t_values = np.zeros(n_steps + 1)
    y_values = np.zeros(n_steps + 1)
    
    # Initial values
    t_values[0] = t0
    y_values[0] = y0

    # Iterative Euler calculation
    for i in range(n_steps):
        y_values[i + 1] = y_values[i] + h * f(t_values[i], y_values[i])
        t_values[i + 1] = t_values[i] + h

    return t_values, y_values

# -----------------------------
# Parameters
# -----------------------------
t0 = 0.0
y0 = 1.0
h = 0.25

t_end = 3.0

# Run Euler method
t_euler, y_euler = euler_method(f, t0, y0, h, t_end)

# Exact solution for comparison
y_true = y_exact(t_euler)

# -----------------------------
# Print Step-by-Step Results
# -----------------------------
print("------------------------------------------------------")
print("   Step |    t_n   |     y_n (Euler)   |   y_exact   |   Error")
print("------------------------------------------------------")
for i in range(len(t_euler)):
    error = abs(y_true[i] - y_euler[i])
    print(f"{i:7d} | {t_euler[i]:8.3f} | {y_euler[i]:15.6f} | {y_true[i]:10.6f} | {error:8.6f}")
print("------------------------------------------------------")

# -----------------------------
# Plot Euler vs Exact solution
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(t_euler, y_euler, 'bo-', label="Euler Approximation")
plt.plot(t_euler, y_true, 'r--', label="Exact Solution")
plt.title("Euler Method for dy/dt = -2y")
plt.xlabel("Time t")
plt.ylabel("y(t)")
plt.legend()
plt.grid(True)
plt.show()
