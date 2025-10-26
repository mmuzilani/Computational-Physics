# ⚛️ Euler Method for Solving ODEs (Step-by-Step with h = 0.25)
**Author:** Md. Mahiuddin Zilani  
**Date:** October 26, 2025  
**Field:** Computational Mathematics for Physics  

---

## 🧠 Introduction

This project demonstrates the **Euler Method**, a simple and powerful **numerical technique** for solving first-order Ordinary Differential Equations (ODEs).  
It prints each computation step in a **mathematical table format** and compares the **Euler approximation** with the **analytical (exact)** solution.

The program solves the ODE:

\[
\frac{dy}{dt} = -2y, \quad y(0) = 1
\]

---

## 📘 Theory

Euler Method approximates the next value of \( y \) using the formula:

\[
y_{n+1} = y_n + h \cdot f(t_n, y_n)
\]

Where:
| Symbol | Meaning |
|:--|:--|
| \( y_{n+1} \) | Approximate value of \( y \) at next step |
| \( y_n \) | Current value of \( y \) |
| \( h \) | Step size |
| \( f(t_n, y_n) \) | Derivative (slope) at current point |

🧩 **In this example:**
\[
f(t, y) = -2y, \quad h = 0.25, \quad y(0) = 1
\]

The **exact solution** of this ODE is:
\[
y(t) = e^{-2t}
\]

---

## ⚙️ Parameters

| Parameter | Value | Description |
|:--|:--|:--|
| `t0` | 0.0 | Initial time |
| `y0` | 1.0 | Initial condition |
| `h` | 0.25 | Step size |
| `t_end` | 3.0 | Final time |
| `f(t, y)` | `-2*y` | Derivative function |

---

## 💻 Code Overview

```python
def f(t, y):
    return -2 * y  # ODE definition

def y_exact(t):
    return np.exp(-2 * t)  # Analytical solution

def euler_method(f, t0, y0, h, t_end):
    n_steps = int((t_end - t0) / h)
    t_values = np.zeros(n_steps + 1)
    y_values = np.zeros(n_steps + 1)
    t_values[0], y_values[0] = t0, y0

    for i in range(n_steps):
        y_values[i + 1] = y_values[i] + h * f(t_values[i], y_values*

