# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 19:59:02 2022

@author: damia
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Espiral de arquímedes
# =============================================================================
points = 1000
theta = np.linspace(0,20*np.pi,points)
T = np.zeros((points,2))

def pintar_espiral():
    T[:,0] = theta*np.cos(theta)
    T[:,1] = theta*np.sin(theta)
    
pintar_espiral()

plt.plot(T[:,0],T[:,1])
