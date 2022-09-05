# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 19:59:01 2022

@author: damia
"""

from matplotlib import pyplot as plt

# =============================================================================
# Números primos
# =============================================================================

def primos():
    
    numero = 2
    
    yield numero
    
    while True: 
        temporal = numero
        while True:
            temporal += 1
            contador = 1
            contador_de_divisores = 0
            
            while contador <= temporal:
                
                if temporal % contador == 0:
                    contador_de_divisores += 1
                    
                if contador_de_divisores > 2:
                    break 
                
                contador += 1
            
            if contador_de_divisores == 2:
                yield temporal
                           
p = primos()
Prim10 = [next(p) for i in range(10)]
Primos = [next(p) for i in range(1000)]

print("Los primeros diez números primos son: "+ str(Prim10))
posicion = []

l = 1

while l < 1001:
    posicion.append(l)
    l +=1
    
plt.plot(posicion,Primos)  
