# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 10:29:34 2022

@author: damia
"""
import numpy as np

class Integrator:
    
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.h = self.x[1] - self.x[0]
        self.integral = 0.
        
    def Trapezoid(self):
        self.integral = 0.
        self.integral += 0.5*(self.y[0] + self.y[-1])
        self.integral += np.sum( self.y[1:-1] )
        return self.integral*self.h
        
    def GetTrapezoidError(self,f):
        d = (f( self.x + self.h ) - 2*f(self.x) + f( self.x - self.h))/self.h**2 
        max_ = np.max(np.abs(d))
        self.error = (max_* (self.x[-1]-self.x[0])**3 )/(12*(len(self.x)-1)**2)
        return self.error   

exp = lambda x: np.exp(-(x**2))
n_points = 1
x = np.linspace(0,1,n_points+1)
y = exp(x)
int1 = Integrator(x,y)        
error = int1.GetTrapezoidError(exp) 

while error > 5e-3:
    n_points += 1
    x = np.linspace(0,1,n_points+1)
    int1 = Integrator(x,y)        
    error = int1.GetTrapezoidError(exp)
        
x = np.linspace(0,1,n_points+1)
y = exp(x)
intf = Integrator(x,y)        
respuesta = intf.Trapezoid()
 
print("1. La integral definida desde 0 a 1 de la función e^{-x^{2}} es: "+str(round(respuesta,7))+\
      ".\n\n2. Se llega a esto aplicando el método de trapecios con "+str(round(n_points,0)),\
      "trapecios.\n\n3. Esta cuenta con un error de: "+str(round(int1.GetTrapezoidError(exp),7))+".")