# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 15:24:07 2022

@author: damia
"""
# =============================================================================
# Punto 4:
# =============================================================================
import matplotlib.pyplot as plt

def productoria(range_):
    prod = 1
    for i in range(range_):
        prod *= (365-i)/365
    return(prod)    
    
list_ = [] 
n = []     
for i in range(80):
    list_.append(productoria(i))
    n.append(i)
    
plt.plot(n,list_,c='c',linestyle='-')
plt.xlabel('Número de cumpleaños distintos',c='k')
plt.ylabel('Probabilidad del suceso',c='k')