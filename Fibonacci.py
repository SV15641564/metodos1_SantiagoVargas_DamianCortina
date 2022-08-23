# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 19:33:54 2022

@author: damia
"""

import matplotlib.pyplot as plt

# =============================================================================
# Fibonacci
# =============================================================================

rango = 22
fib = [0,1]
for i in range(rango - 2):
    fib.append(fib[-1] + fib[-2])
    
fib.pop(0)
fib.pop(1)    

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]   

plt.plot(lista,fib)
