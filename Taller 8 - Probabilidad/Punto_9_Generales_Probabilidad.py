# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 16:14:54 2022

@author: damia
"""
# =============================================================================
# Punto 9:
# =============================================================================
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

N = int(1e5)
ncoins = 4
events = [-1,1]
Sample = np.zeros((N,ncoins))

p2 = np.linspace(0.1,0.5,100)
p1 = np.linspace(0.1,0.9,100) 
P1,P2 = np.meshgrid(p1,p2)
Z = np.empty_like(P1)
Z = (P1*P2+2*(1-P1)*P2+2*P1*(1-P2)+(1-P1)*(1-P2))/4

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1, 1, 1, projection='3d')    
surf = ax.plot_surface(P1,P2,Z,cmap=cm.coolwarm,antialiased=True)
fig.colorbar(surf, shrink=0.6, aspect=10)   
ax.set_xlabel("P1",c='k',fontsize=15)
fig.suptitle('Superficie de Probabilidad',fontsize=30,c='k')
ax.set_ylabel("\n\n\nP2",c='k',fontsize=15)
ax.view_init(45,85)