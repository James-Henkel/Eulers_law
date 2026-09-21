# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:54:08 2026

@author: james
"""

import numpy as np
import matplotlib.pyplot as plt

tmax = 35 

h = 0.05
t_array = np.arange(0, tmax + h/2, h)
num_steps = len(t_array)

x_array = np.zeros(num_steps)
v_array = np.zeros(num_steps)
    
x_array[0] = 0
v_array[0] = 1
    
for i in range(1, num_steps):
    t = t_array[i-1]
    xinit = x_array[i-1] + h * v_array[i-1]
    vinit = v_array[i-1] - h * x_array[i-1]
            
    x_array[i] = x_array[i-1] + 0.5*h*(v_array[i-1]+vinit)
    v_array[i] = v_array[i-1] - 0.5*h*(x_array[i-1]+xinit)

plt.plot(t_array, x_array, label=f'Euler for position')
plt.plot(t_array, v_array, label=f'Euler for velocity')
plt.plot(t_array, np.sin(t_array), 'k--', label=f'Exact position line')
plt.plot(t_array, np.cos(t_array), 'k--', label=f'Exact velocity line')
plt.title("Euler Method vs Exact Solution (Coupled Equations)")
plt.xlabel("Time (t)")
plt.ylabel("x (Position)")
plt.legend()
plt.show()