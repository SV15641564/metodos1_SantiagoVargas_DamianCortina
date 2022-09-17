# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 12:12:15 2022

@author: damia
"""
import numpy as np
import sympy as sym
from tqdm import tqdm
import matplotlib.pyplot as plt

def GetLaguerre(n):
    x = sym.Symbol('x',Real=True)
    y = sym.Symbol('y',Real=True)
    y = sym.exp(-x)*x**n
    pol = sym.exp(x)*sym.diff(y,x,n)/(np.math.factorial(n))
    return pol

n_list = [2,3,4,5,6,7,8,9,10]
Integration_list = []
X = sym.Symbol('x',Real=True)
h = 0.001
for n in tqdm(range(2,11)):
    
    f = GetLaguerre(n)
    
    def derivada(f,x):
      return (f.subs(X,x+h)-f.subs(X,x-h))/(2*h)
    
    def GetNewtonMethod(f,df,xn,itmax=1000,precision=1e-9):
        error = 1
        it = 0
        while error > precision and it < itmax: 
            xn1 = xn - f.subs(X,xn)/df(f,xn)
            error = np.abs(f.subs(X,xn)/df(f,xn))
            xn = xn1
            it += 1
        if it == itmax:
            return False
        else:
            return xn
    
    def GetAllRoots(x,tolerancia=8):
        Roots = np.array([])
        for i in x:
            #print("Ciclo total: "+str(n-1)+"/9")
            root = GetNewtonMethod(f,derivada,i)
            if root != False:
                croot = round(root,tolerancia)
                if round(croot,13) not in Roots:
                    if np.abs(croot) < 0.001:
                        Roots = np.append(Roots,round(croot,13))
                    else:   
                        Roots = np.append(Roots,round(croot,13))                   
        Roots.sort()
        return Roots
    
    espacio_x = np.linspace(0,30,30)
    Roots = GetAllRoots(espacio_x)
    Laguerre = []
    DerLaguerre = []
    xsym = sym.Symbol('x',Real=True)
    n_polynomials=11
    
    for i in range(n_polynomials+1):
        poly = GetLaguerre(i)
        Laguerre.append(poly)
        DerLaguerre.append(sym.diff(poly,xsym))
        
    def GetRootsPolynomial(symbol,n,xi,poly,dpoly):
        pn = sym.lambdify([symbol],poly[n],'numpy')
        dpn = sym.lambdify([symbol],dpoly[n],'numpy')
        Roots = GetAllRoots(pn,dpn,xi)
        if n%2 != 0:
          Roots = np.insert(Roots,len(Roots),0)  
        return Roots
    
    xi = np.linspace(-1,1,100)
       
    def GetWeights(Roots,Dpoly):
        Weights = []
        x = sym.Symbol('x',Real=True)
        pn1 = sym.lambdify([x],Laguerre[n+1],'numpy')
        for r in Roots:
            Weights.append(r/(((n+1)**2)*(pn1(r))**2))
        return Weights
        
    Weights = GetWeights(Roots,DerLaguerre)
    integral = 0
    
    f = lambda x: ((x**3)/(np.exp(x)-1))
    
    for n_ in range(n):
        integral += Weights[n_]*f(float(Roots[n_]))*np.exp(float(Roots[n_]))
    Integration_list.append(integral/((1/15)*np.pi**4))
    
plt.scatter(n_list,Integration_list,color='c')