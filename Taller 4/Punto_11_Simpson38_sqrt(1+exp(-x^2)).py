# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 12:37:22 2022

@author: damia
"""
print("Se demora de 3 a 5 segundos en cargar, pues se le pidió que contara con 1 millón de puntos...\n\n")

import numpy as np

class Integrator:
    
    def __init__(self, x,y): 
        self.x = x
        self.y = y
        self.h = (self.x[-1] - self.x[0])/n_points
        self.integral = 0.
        self.x_space =  np.linspace(0,3*self.h,4)
    
    def Simpson38(self):
        self.integral += self.y[0] + self.y[-1]    
        for i in range(1,len(y[1:-1])):
            if i%3 == 0:
                self.integral += 2*f(x[0] + (i)*self.h)
            else:
                self.integral += 3*f(x[0] + (i)*self.h)
        return self.integral * 3 * self.h / 8        

f = lambda x: np.sqrt(1+np.exp(-x**(2)))
n_points = 1000000
x = np.linspace(-1,1,n_points)
y = f(x)
int1 = Integrator(x,y)
value = int1.Simpson38()
err = round((2.6388571169 - value),7) #Valor_guía - Valor_simpson3/8

print("El área bajo la curva de la función sqrt(1+exp(-x^2)) en el rango (-1,1) es: "+str(value)\
      +"\n\n\nEsto cuenta con un error de "+f"{err:.6f}"+" o "+str(err)+", con respecto al valor dado en la guía de clase.")