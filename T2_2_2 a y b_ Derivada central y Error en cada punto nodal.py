# -*- coding: utf-8 -*-

from math import exp
import numpy
import matplotlib.pyplot as plt

func = lambda x: x/(exp(x**2)*(1 + exp(-(x**2))**1.5))
orig = lambda x: (1 + exp(-(x**2)))**(-0.5)
est_func = lambda x: 10*(orig(x+0.05) - orig(x-0.05))

"""error nodal"""
error = lambda x, y: abs(numpy.subtract(x, y))

x = numpy.linspace(-10, 10, 401)
est = numpy.array(list(map(est_func, x)))

nodal=(error(list(map(func, x)), list(map(est_func, x))))

plt.plot(est)

"""Use este print para imprimir cada valor de la derivada (central)
 en el intervalo -10 a 10"""

#print(est)

"""Use este print para imprimir el error por punto nodal"""

#print(nodal)

"""Nótese que los ordenes de magnitud son extremadamente pequeños, por ende,
el método es exacto"""
