# -*- coding: utf-8 -*-
"""
Spyder Editor

Code For Eulers exp. week1 
"""

import numpy as np
import matplotlib.pyplot as plt


dt = 0.25
t_max = 10
tau = 2.0

t = 0.0
N = 10
N0 = 10

t_list = [t]
N_list = [N]
N2_list = [N0 * np.exp(-t/tau)]

# --- Start Loop ---
while abs(t - t_max) > dt / 2:
    N = N - (N / tau) * dt
    
    t = t + dt
    N2 = N0 * np.exp(-t/tau)
    
    t_list.append(t)
    N_list.append(N)
    N2_list.append(N2)

t_values = np.array(t_list)
N_values = np.array(N_list)
N2_values = np.array(N2_list)

# --- Plot Graph ---
plt.plot(t_values, N_values, linestyle='-', color='b', label="Expected Values")
plt.plot(t_values, N2_values, linestyle='--', color='r', label="Calculated Values")

# Add labels, title, and a legend
plt.title("Radioactive Decay using Euler's Method")
plt.xlabel("Time (t)")
plt.ylabel("Quantity (N)")
plt.legend()    # This shows the labels from the plt.plot() calls
plt.show()


diff = N2_values - N_values

plt.plot(t_values, diff, linestyle='-', color = 'black')
plt.title("Difference between CAluculated and Expected Values for Euler's Method")
plt.xlabel("Time (t)")
plt.ylabel("Quantity (N)")
plt.show()    