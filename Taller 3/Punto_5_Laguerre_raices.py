# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 13:21:53 2022

@author: damia
"""
import sympy as sym
import numpy as np
h = 0.001
lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# =============================================================================
# ¡Por favor esperar unos segundos, como son tantos polinomios se demora un poco!
# =============================================================================

for item in lista:
    
    def Laguerre(n):
    
        x = sym.Symbol('x',Real=True)
        y = sym.Symbol('y',Real=True)
    
        y = sym.exp(-x)*x**n
    
        p = sym.exp(x)*sym.diff(y,x,n)/(np.math.factorial(n))
    
        return p
    
    X = sym.Symbol('x',Real=True)
    f = Laguerre(item)
    
    
    def derivada(f,x):
      return (f.subs(X,x+h)-f.subs(X,x-h))/(2*h)
    
    
    
    def GetNewtonMethod(f,df,xn,itmax=1000,precision=1e-5):
        error = 1
        it = 0
        while error > precision and it < itmax: 
            try:
                xn1 = xn - f.subs(X,xn)/df(f,xn)
                error = np.abs(f.subs(X,xn)/df(f,xn))
            except ZeroDivisionError:
                print('Hay un error de división por cero.')     
            xn = xn1
            it += 1
        if it == itmax:
            return False
        else:
            return xn
    
    
    def GetAllRoots(x,tolerancia=8):
        Roots = np.array([])
        for i in x:
            root = GetNewtonMethod(f,derivada,i)
            if root != False:
                croot = round(root,tolerancia)
                if round(croot,2) not in Roots:
                    if np.abs(croot) < 0.001:
                        Roots = np.append(Roots,round(croot,8))
                    else:   
                        Roots = np.append(Roots,round(croot,8))
                        
        Roots.sort()
        return Roots
    
    
    espacio_x = np.linspace(-1,100,30)
    Roots = GetAllRoots(espacio_x)
    
    
    
    resultado = []
    for i in Roots:
        if i not in resultado:
            resultado.append(i)
    
            
    if item == 0:
        print("El polinomio de grado 0 no tiene raíces.\n")
        
    else:
        print("Los ceros del polinomio de grado",item,"son:",resultado,"\n")
        
        
    
