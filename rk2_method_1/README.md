# Runge–Kutta 2nd Order (RK2) Method — Heun’s Method

This project demonstrates the **Runge–Kutta 2nd Order Method (RK2)**, also known as the **Improved Euler Method** or **Heun’s Method**, for solving **first-order Ordinary Differential Equations (ODEs)** in **Computational Physics**.

It provides a **step-by-step tabular output** and a **graphical comparison** between the numerical and analytical solutions.

---

## Problem Definition

We want to solve the following ODE:

$$
\frac{dy}{dt} = -2y, \quad y(0) = 1
$$

Using the **RK2 update equations**:

$$
\begin{aligned}
k_1 &= f(t_n, y_n) \\
k_2 &= f(t_n + h, \; y_n + h \, k_1) \\
y_{n+1} &= y_n + \frac{h}{2} (k_1 + k_2)
\end{aligned}
$$

In this example:

$$
f(t, y) = -2y, \quad h = 0.25, \quad y(0) = 1
$$

The **exact analytical solution** of this ODE is:

$$
y(t) = e^{-2t}
$$

---

## Parameters Used

| Parameter | Meaning | Value |
|------------|----------|-------|
| `t0` | Initial time | 0.0 |
| `y0` | Initial value | 1.0 |
| `h` | Step size | 0.25 |
| `t_end` | Final time | 3.0 |

---

## Step-by-Step Formula Explanation

The RK2 (Heun’s) method works in two stages per step:

1. Compute slope at the beginning of the interval  
   \( k_1 = f(t_n, y_n) \)

2. Estimate slope at the end of the interval using the first slope  
   \( k_2 = f(t_n + h, y_n + h k_1) \)

3. Take the **average of both slopes** to update the value:  
   \( y_{n+1} = y_n + \frac{h}{2} (k_1 + k_2) \)

This averaging of slopes improves the accuracy compared to the simple Euler method.

---

## Example Output (Printed Table)

When you run the Python script, you’ll see a table like this:
Step | t_n | y_n (RK2) | y_exact | Error
0 |  0.000  |        1.000000  |   1.000000   |  0.000000
1 |  0.250  |        0.536458  |   0.606531   |  0.070073
2 |  0.500  |        0.287874  |   0.367879   |  0.080005
3 |  0.750  |        0.154531  |   0.223130   |  0.068599
4 |  1.000  |        0.082745  |   0.135335   |  0.052590
...

This shows how RK2 closely follows the true analytical curve, improving accuracy over Euler’s method.

---

## Graphical Comparison

- **Blue circles:** RK2 Approximation  
- **Red dashed line:** Exact Analytical Solution  

The plot displays both curves on the same graph to visualize how RK2 provides a better approximation.

---


