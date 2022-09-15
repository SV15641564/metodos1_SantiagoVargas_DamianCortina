# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:06:48 2022

@author: damia
"""
import numpy as np
import sympy as sym

def GetNewtonMethod(f,df,xn,itmax = 100000, precision=1e-13): #importado de anteriores talleres.
    error = 0.001
    it = 0
    while error > precision and it < itmax:
        xn1 = xn - f(xn)/df(xn)
        error = np.abs(f(xn)/df(xn))
        xn  = xn1
        it += 1
    if it == itmax:
        return False
    else:
        return round(xn,13)
    
def GetAllRoots(f,df,x, tolerancia=15): #importado de anteriores talleres.
    Roots = np.array([])
    for i in x:
        root = GetNewtonMethod(f,df,i)
        if root != False:
            croot = np.round( root, tolerancia ) 
            if croot not in Roots:
                Roots = np.append( Roots, croot )  
    Roots.sort()
    return Roots

def GetLegendre(n): #importado de anteriores talleres.
    x = sym.Symbol('x',Real=True)
    y = sym.Symbol('y',Real=True)
    y = (x**2 - 1)**n
    pol = sym.diff(y,x,n)/(2**n * np.math.factorial(n))
    return pol

Legendre = []
DerLegendre = []
xsym = sym.Symbol('x',Real=True)
n_polynomials=20

for i in range(n_polynomials+1):
    poly = GetLegendre(i)
    Legendre.append(poly)
    DerLegendre.append(sym.diff(poly,xsym))
    
def GetRootsPolynomial(symbol,n,xi,poly,dpoly):
    pn = sym.lambdify([symbol],poly[n],'numpy')
    dpn = sym.lambdify([symbol],dpoly[n],'numpy')
    Roots = GetAllRoots(pn,dpn,xi)
    if n%2 != 0:
      Roots = np.insert(Roots,len(Roots),0)  
    return Roots

xi = np.linspace(-1,1,100)
for n in range(2,4):

    Roots = GetRootsPolynomial(xsym,n,xi,Legendre,DerLegendre)
    
    def GetWeights(Roots,Dpoly):
        Weights = []
        x = sym.Symbol('x',Real=True)
        dpn = sym.lambdify([x],Dpoly[n],'numpy')
        for r in Roots:
            Weights.append( 2/(( 1- r**2 )*dpn(r)**2) )
        return Weights
    
    Weights = GetWeights(Roots,DerLegendre)
       
    a = 1
    b = 2
    f = lambda x : x**(-2)
    t = 0.5*((b-a)*Roots + a + b)
    Integral = 0.5*(b-a)*np.sum(Weights*f(t))
    print("La integral de la función x^(-2) usando el método de Gauss-Legendre con",n,"puntos es:",\
          round(Integral,6),"\n\n")