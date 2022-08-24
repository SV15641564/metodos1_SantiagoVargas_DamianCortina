# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 19:59:01 2022

@author: damia
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Número Áureo
# =============================================================================
def fib(n:int):
    a=0
    b=1
    for i in range (n):
        a, b = b, a + b
    return a
#Esta función calcula la suma de n primeros números Fibonacci.


def fi(n:int):
    return fib(n) / fib(n-1)
#Esta función usa la anterior función para calcular el número Áureo en base a la suma
#de una cantdad n de números Fibonacci.
  
def aureo_real():  
    aureo_real = (1 + np.sqrt(5))/2
    return aureo_real


x = range(2,18)
plt.plot(x, [fi(i) for i in x], [aureo_real() for i in x])