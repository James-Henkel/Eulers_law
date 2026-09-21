# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:54:08 2026

@author: james
"""

import numpy as np
import matplotlib.pyplot as plt

tmax = 35 

# The problem asks to vary h from 0.05 to 0.0005
h_values = [0.05, 0.01, 0.001, 0.0005]


# Loop through each time step size
for h in h_values:
    # 1. Create Time Array
    t_array = np.arange(0, tmax + h/2, h)
    num_steps = len(t_array)
    
    # 2. Initialize Solution Arrays (x and y)
    # x represents position, y represents velocity
    x_array = np.zeros(num_steps)
    y_array = np.zeros(num_steps)
    
    # 3. Initial Conditions
    # Based on equation 27a: x = sin(y). If we start at t=0, sin(0)=0.
    # Let's start with x=0. To make the sine wave move, we need an initial velocity.
    # Let's set x=0, y=1 (so x will become sin(t)).
    x_array[0] = 0.0
    y_array[0] = 1.0
    
    # 4. Euler Method Loop
    # We must update x and y simultaneously using the PREVIOUS values
    for i in range(1, num_steps):
        t = t_array[i-1]
        
        # Current values
        x_curr = x_array[i-1]
        y_curr = y_array[i-1]
        
        # Derivatives from Equation 27
        # dx/dt = y
        dxdt = y_array[i-1]
        # dy/dt = -x
        dydt = -x_array[i-1]
        
        # Update steps
        x_array[i] = x_curr + h * dxdt
        y_array[i] = y_curr + h * dydt

    # 5. Plotting
    # The prompt asks to compare x-tilde vs exact solution.
    # Exact solution for x with these ICs is sin(t).
    if h == 0.05:
        # Plot the exact solution only once (for reference)
        plt.plot(t_array, np.sin(t_array), 'k--', linewidth=2, label='Exact: sin(t)')
    
    plt.plot(t_array, x_array, label=f'Euler h={h}')

# Formatting the Graph
plt.title("Euler Method vs Exact Solution (Coupled Equations)")
plt.xlabel("Time (t)")
plt.ylabel("x (Position)")
plt.legend()
plt.show()

diff_array = x_array - np.sin(t_array)
plt.plot(t_array, diff_array)
plt.title("Euler Method vs Exact Solution (Difference of Solutions)")
plt.xlabel("Time (t)")
plt.ylabel("x (Position)")
plt.legend()
plt.show()

