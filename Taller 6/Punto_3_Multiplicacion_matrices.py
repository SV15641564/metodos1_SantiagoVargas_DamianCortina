# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 09:26:02 2022

@author: damia
"""
import numpy as np

M = np.array([[1.,0.,0.],[5.,1.,0.],[-2.,3.,1.]])
A = np.array([[4.,-2.,1.],[0.,3.,7.],[0.,0.,2.]])

m,n = len(M),len(A[0])
Sol = np.zeros((m,n))

if len(M[0]) != len(A):
    print("El número de columnas de la primera matriz debe coincidir con el número de filas de la segunda matriz.")
else:
    for i in range(len(M)):
        for j in range(len(M[i])):
            for k in range(len(A)):
                Sol[i,j] += M[i,k]*A[k,j] #La posición i,j en la solución es la suma de los coeficientes de la fila i
                                          #en la matriz M multiplicados por los de la columna j en la mariz A, usamos 
                                          #k para correr dentro de estas filas y columnas.
    print("La solución a la multiplicación es:\n\n",Sol)