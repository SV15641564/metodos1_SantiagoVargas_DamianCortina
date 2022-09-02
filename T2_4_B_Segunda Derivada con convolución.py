# -*- coding: utf-8 -*-
from math import exp
import numpy
import matplotlib.pyplot as plt

func = lambda x: x/(exp(x**2)*(1 + exp(-(x**2))**1.5))
orig = lambda x: (1 + exp(-(x**2)))**(-0.5)

x = numpy.linspace(-10, 10, 401)

#------------------------------------------------------------------------------
# SEGUNDA DERIVADA CON CONVOLUCION
#------------------------------------------------------------------------------
M = [1, -2, 1]
f = numpy.array(list(map(orig, x)))
r = numpy.zeros(f.size)
for i in range(f.size-2):
    r[i+1] = 10*(numpy.dot(f[i:i+3], M))
    
    """Use este plot para graficar la derivada con convolución"""
#plt.plot(x, r)