# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 19:59:02 2022

@author: damia
"""
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Figuras de Lissajous
# =============================================================================
phi = [0, np.pi/4, np.pi/2]
theta = np.linspace(0, 2*np.pi, 100)

for i in range(0,3):
    for u in range(1,6):
        for y in range(1,6):
            if y >= u:
                eje_x = np.cos(y*theta+phi[i])
                eje_y = np.sin(u*theta)
                fig = plt.subplot(6,5,u*5+y)
                y += 1
                plt.plot(eje_x,eje_y)                
