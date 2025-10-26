# ⚛️ Euler Method for Solving ODEs (Step-by-Step with h = 0.25)
**Author:** Md. Mahiuddin Zilani  

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

The program:

Solves the ODE numerically using Euler’s formula.

Compares each step with the exact analytical value.

Prints a table of results with errors.

Plots both curves for visual comparison.

---
------------------------------------------------------
   Step |    t_n   |     y_n (Euler)   |   y_exact   |   Error
------------------------------------------------------
      0 |    0.000 |        1.000000 |   1.000000 | 0.000000
      1 |    0.250 |        0.500000 |   0.606531 | 0.106531
      2 |    0.500 |        0.250000 |   0.367879 | 0.117879
      3 |    0.750 |        0.125000 |   0.223130 | 0.098130
      4 |    1.000 |        0.062500 |   0.135335 | 0.072835
      5 |    1.250 |        0.031250 |   0.082085 | 0.050835
      6 |    1.500 |        0.015625 |   0.049787 | 0.034162
      7 |    1.750 |        0.007812 |   0.030197 | 0.022385
      8 |    2.000 |        0.003906 |   0.018316 | 0.014410
      9 |    2.250 |        0.001953 |   0.011109 | 0.009156
     10 |    2.500 |        0.000977 |   0.006738 | 0.005761
     11 |    2.750 |        0.000488 |   0.004086 | 0.003598
     12 |    3.000 |        0.000244 |   0.002479 | 0.002235
------------------------------------------------------

raphical Result

The graph shows:

Blue Line (dots) → Euler Method approximation

Red Dashed Line → Exact analytical solution 
y=e−2t
y=e
−2t

When h = 0.25, the Euler method gives a fairly accurate result, but you can observe small deviations due to truncation errors.
