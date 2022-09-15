# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 20:31:08 2022

@author: damia
"""
import numpy as np
import sympy as sym

X = np.array([122,222,322,422]) 
Y = np.array([0.001,22,34,4])

def Lagrange(x,xi,j):   
    prod = 1.0
    n = len(xi)
    for i in range(n):
        if i != j:
            prod *= (x - xi[i])/(xi[j]-xi[i]) 
    return prod

def Poly(x,xi,yi):    
    Sum = 0.
    n = len(xi)        
    for j in range(n):
        Sum += yi[j]*Lagrange(x,xi,j)        
    return Sum

h = (X[-1]-X[0])/3
x_space = np.linspace(0,3*h,4) #Espacio de definición de la integral.
y = Poly(x_space,X,Y)
xsym = sym.Symbol('x')
f = Poly(xsym,X,Y).expand()

Integration_Lagrange_answer = ((3*h)/8)*(f.subs(xsym,x_space[0])+(3*(f.subs(xsym,(2*x_space[0] + \
               x_space[-1])/3)))+(3*(f.subs(xsym,(x_space[0] + 2*x_space[-1])/3)))+\
               f.subs(xsym,x_space[-1])) 
       
Sympy_answer = sym.integrate(f, (xsym,x_space[0],x_space[-1]))

print("\na) Se corrobora que es cierto, pues integrando la función con sym.integrate(f,(x,a,b)) da: "+str(Sympy_answer))
print("\nUsando la fórmula 3h/8(f(a)+3f(2a+b/3)+3f(a+2b/3)+f(b)) da lo siguiente: "+str(Integration_Lagrange_answer))
print("\nLa resta de ambas respuestas da un total de: "+str(float(round(Sympy_answer-Integration_Lagrange_answer,8))))

midpoint1, midpoint2 = (2*X[0] + X[-1])/3, (X[0] + 2*X[-1])/3

print("\n=======================================================\
      \n\nb) (2a+b)/3 y (a+2b)/3 son puntos intermedios pues se cumple que su resta es: "\
      +str(np.abs(midpoint2-midpoint1)))
print("\nPor otra parte, el valor de h es: "+str(h))
print("\nLa resta de ambas cosas da un total de: "+str(np.abs(float(round(np.abs(midpoint2-midpoint1)-h,8)))))
print("\n=======================================================\
      \n\nEstos valores están sujetos a los puntos en X y Y dados para generar el polinomio.")
