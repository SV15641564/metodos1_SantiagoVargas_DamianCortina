# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 19:54:40 2022

@author: damia
"""
import numpy as np

# =============================================================================
# Punto A:
# =============================================================================
u1 = [3,1,0,1]
u2 = [1,2,1,1]
u3 = [-1,0,2,-1]
b = np.array([[-3,-3,8,9]]).T
A = np.array([u1,u2,u3]).T
ATxA_inv = np.linalg.inv(A.T@A)
Solution_to_x_vector = ATxA_inv@A.T@b
Solution_to_problem = A@Solution_to_x_vector.round()
print("\nA) La solución para la proyección pedida en el problema de mínimos cuadrado es:\n",Solution_to_problem.T)


# =============================================================================
# Punto B:
# =============================================================================
v1 = np.array(u1)
v2 = np.array(u2) - ((np.array(u2)@v1)/(v1@v1))*v1
v3 = np.array(u3) - ((np.array(u3)@v1)/(v1@v1))*v1 - ((np.array(u3)@v2)/(v2@v2))*v2
v1 = v1/(np.linalg.norm(v1))
v2 = v2/(np.linalg.norm(v2))
v3 = v3/(np.linalg.norm(v3))
c1 = b.T@v1
c2 = b.T@v2
c3 = b.T@v3
Solution_to_problem2 = (c1*v1)+(c2*v2)+(c3*v3)
print("\n\nB) La solución para la proyección pedida en el problema de ortonormalización es:\n",Solution_to_problem2)