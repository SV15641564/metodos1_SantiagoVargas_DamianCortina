# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 10:24:16 2022

@author: damia
"""

import numpy as np
h = 0.001

# =============================================================================
# Primera parte:
# =============================================================================
def funcion(x):
  return 3*(x**5)+5*(x**4)-(x**3)



def derivada(f,x):
  return (f(x+h)-f(x-h))/(2*h)



def GetNewtonMethod(f,df,xn,itmax=1000,precision=1e-5):
    error = 1
    it = 0
    while error > precision and it < itmax: 
        try:
            xn1 = xn - f(xn)/df(f,xn)
            error = np.abs(f(xn)/df(f,xn))
        except ZeroDivisionError:
            print('Division por cero')     
        xn = xn1
        it += 1
    if it == itmax:
        return False
    else:
        return xn



def GetAllRoots(x,tolerancia=8):
    Roots = np.array([])
    for i in x:
        root = GetNewtonMethod(funcion,derivada,i)
        if root != False:
            croot = np.round( root, tolerancia )
            if round(croot,5) not in Roots:
                if np.abs(croot) < 0.001:
                    Roots = np.append(Roots,round(croot,8))
                else:   
                    Roots = np.append(Roots,round(croot,8))
                    
    Roots.sort()
    return Roots


espacio_x = np.linspace(-2,1,30)
Roots = GetAllRoots(espacio_x)



resultado = []
for i in Roots:
    if i not in resultado:
        resultado.append(i)

indices_a_eliminar = []

for i in range(len(resultado)):
    if np.abs(round(resultado[i-1],4))==np.abs(round(resultado[i],4)):
        indices_a_eliminar.append(resultado[i])
    else:
        None

for i in indices_a_eliminar:
    resultado.remove(i)    
        
print("Los ceros del polinomio son:",resultado)
        
        
        
    