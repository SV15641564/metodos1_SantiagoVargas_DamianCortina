# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 17:12:36 2022

@author: damia
"""
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from tqdm import tqdm

# =============================================================================
# Punto A:
# =============================================================================
A = np.array([[2,1,1],[-1,2,1]])
B = np.array([[2,1,4]])
A = A.T
B = B.T
ATxA_inv = np.linalg.inv(A.T@A)
Solution = ATxA_inv@A.T@B
print("\nA) La solución que mejor se ajusta al problema es el punto: ("+str(Solution[0,0])+","+str(Solution[1,0])+").\n")

x = np.linspace(0,5,333)
y1 = 2*x-2
y2 = (1-x)/2
y3 = 4-x

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.plot(x,y1, 'tab:grey')
plt.plot(x,y2, 'tab:grey')
plt.plot(x,y3, 'tab:grey')
plt.scatter(Solution[0],Solution[1],c='c')
plt.show()


        
# =============================================================================
# Punto B:
# =============================================================================
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1, 1, 1, projection='3d')
X = np.arange(-5, 5, 0.03)
Y = np.arange(-5, 5, 0.03)
X, Y = np.meshgrid(X, Y)
Z = np.sqrt((2*X-Y-2)**2+(X+2*Y-1)**2+(X+Y-4)**2) 
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.magma,linewidth=0, antialiased=False,)
ax.set_zlim(0, 22.5)
ax.view_init(7,45) #Se puede rotar el ángulo de cualquier manera, para observar que el punto rojo es solución.
                   #Es más visible si se cambia el segundo número y el primero se mantiene en 0.
menor = 10
for i in range(len(Z)):
    if min(Z[i]) < menor:
        menor = min(Z[i])
    else:
        None
        
ax.scatter(Solution[0],Solution[1],menor,c='r')
fig.colorbar(surf, shrink=0.5, aspect=10)

print("\nB) La imagen puede demorar en salir unos segundos...")
print("\nSe corroboró que se llega a la misma solución, pues se observa que el punto rojo, cuyas coordenadas \
(X,Y,Z) corresponden a (Solución de Ax, Solución de Ay, Menor altura de Bz), coincide exactamente con el \
mínimo de la superificie. \nP = ("+str(Solution[0,0])+","+str(Solution[1,0])+","+str(menor)+").")
