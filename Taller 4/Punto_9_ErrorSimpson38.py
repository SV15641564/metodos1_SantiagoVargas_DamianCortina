# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 09:27:39 2022

@author: damia
"""
import numpy as np
import sympy as sym

X = np.array([-4,-3,-2,-1,1,2,3,4]) 
Y = np.array([222,81/4,4,1/4,1/4,4,81/4,222])

def Lagrange(x,xi,j):   
    prod = 1
    n = len(xi)
    for i in range(n):
        if i != j:
            prod *= (x - xi[i])/(xi[j]-xi[i]) 
    return prod

def Poly(x,xi,yi):    
    Sum = 0
    n = len(xi)        
    for j in range(n):
        Sum += yi[j]*Lagrange(x,xi,j)        
    return Sum

h = (X[-1]-X[0])/3
x_space = np.linspace(0,3*h,4) #Espacio de definición de la integral.
xsym = sym.Symbol('x') 
f = Poly(xsym,X,Y).expand()

function_of_integral = (xsym - x_space[0])*(xsym - x_space[1])*(xsym - x_space[2])*(xsym - x_space[3]) 
                      #(x-x_0)             (x-x_1)             (x-x_2)             (x-x_3)

print("Si se calcula el lado izquierdo de la igualdad se tendría un resultado de: "\
      +str(((sym.diff(f,xsym,4).subs(xsym,x_space[-1]))/np.math.factorial(4))\
      *sym.integrate(function_of_integral,(xsym,x_space[0],x_space[-1]))))
    
print("\nSi se calcula el lado derecho de la igualdad se tendría un resultado de: "\
      +str((-3/80)*h**5*sym.diff(f,xsym,4).subs(xsym,x_space[-1])))
    
print("\nLa resta entre ambos valores redondeada al séptimo decimal es: "+str(round((((sym.diff(f,xsym,4).subs(xsym,x_space[-1]))/np.math.factorial(4))\
     *sym.integrate(function_of_integral,(xsym,x_space[0],x_space[-1]))-((-3/80)*h**5*sym.diff(f,xsym,4).subs(xsym,\
     x_space[-1]))),7)))
    
print("\n=======================================================\
      \n\nEstos valores están sujetos a los puntos en X y Y dados para generar el polinomio.")