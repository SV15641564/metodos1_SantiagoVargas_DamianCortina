# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 17:31:09 2022

@author: damia
"""
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Discretización.
# =============================================================================
n_points = 25

eje_x = np.linspace(-4,4,n_points)
eje_y = np.linspace(-4,4,n_points)

# =============================================================================
# Filtración de puntos adentro del cilindro.
# =============================================================================
R = 2

x, y = np.meshgrid(eje_x, eje_y)
radio_variante = np.sqrt((x)**2 + (y)**2)

for i in range(len(x)):
    for j in range(len(x)):
        if radio_variante[i,j] < R:
            
            x[i,j] = None
            y[i,j] = None

# =============================================================================
# Creación de la función de flujo.            
# =============================================================================
V = 2

def FlujoPotencial(x,y):
    return V*x*(1-((R**2)/(x**2+y**2)))

h = 0.001

# =============================================================================
# Creación de las funciones de derivadas parciales, usando derivada central.
# =============================================================================
def Dx(x,h,y):
    return (FlujoPotencial(x+h,y)-FlujoPotencial(x-h,y))/(2*h)

def Dy(x,h,y):
    return (-1)*(FlujoPotencial(x,y+h)-FlujoPotencial(x,y-h))/(2*h)

Vx = Dx(x,h,y)
Vy = Dy(x,h,y)

# =============================================================================
# Estructura para plotear. Se crea la figura, el ax y la circunferencia roja.
# =============================================================================
fig = plt.figure(figsize=(15,6))
ax = fig.add_subplot(1,2,2)
ax.set_xlabel("x[cm]")
ax.set_ylabel("y[cm]")
circle1 = plt.Circle((0, 0), 2, color='r',fill=False)
ax.add_patch(circle1)

for i in range(len(eje_x)):
    for j in range(len(eje_y)):
        ax.quiver(eje_x[i],eje_y[j],Vx[i,j],Vy[i,j],color='b')








