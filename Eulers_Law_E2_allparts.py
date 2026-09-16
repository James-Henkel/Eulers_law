# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 16:54:35 2026

@author: james
"""

import numpy as np
import matplotlib.pyplot as plt



"""Use of multiple values for x0, or single version of x
    just adjust x0_values for correction                """


# Setup
h = 0.05
tmax = 9

# Array of initial conditions
x0_values = np.array([3, 1, 0, -0.7])
num_x0 = len(x0_values)

# making timer
t_max_9 = np.arange(0, tmax + h/2, h)
num_steps = len(t_max_9)

# creating x_values array, col=time 
x_array = np.zeros((num_x0, num_steps))
x_array[:, 0] = x0_values   # first column = initial conditions

#derivative function
def f(x, t):
    return t - x**2

# running function
for i in range(1, num_steps):
    t = t_max_9[i-1]
    x_array[:, i] = x_array[:, i-1] + h * f(x_array[:, i-1], t)

# graphing
for j in range(num_x0):
    plt.plot(t_max_9, x_array[j, :], label=f"x0 = {x0_values[j]}")

plt.title("Euler's Method for dx/dt = t - x²")
plt.xlabel("Time (t)")
plt.ylabel("x")
plt.legend()
plt.show()




