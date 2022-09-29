# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 07:54:29 2022

@author: damia
"""
import numpy as np

M = np.array([[3,-1,-1],[-1.,3.,1.],[2,1,4]])
b = np.array([1.,3.,7.])

def GetGaußSeidlMethod(A,b,itmax=1000,error = 1e-10):
    M,N = A.shape
    x = np.zeros(N)
    sum_k_iteration = np.zeros_like(x)
    x = [0,0,0]
    it = 0
    residue = np.linalg.norm(b - A@x)
    while (residue > error and it < itmax ):
        it += 1
        for i in range(M):
            sum_ = 0
            for j in range(N):
                if i != j:
                    sum_ += A[i][j]*x[j]
            sum_k_iteration[i] = sum_
            x[i] = (b[i] - sum_k_iteration[i])/A[i,i] #x[i] se calcula directamente después de sum_k_iteration,
                                                      #para usarse calculando la siguiente variable.
        residue = np.linalg.norm(b - A@x)
    return x,it,residue

Xsol,it,error = GetGaußSeidlMethod(M,b)
rounded_Xsol = [round(variable,10) for variable in Xsol]

print("\n1. Para el sistema de ecuaciones usado en clase se obtuvo un vector solución redondeado al décimo "+\
      "decimal (X,Y,Z) =",tuple(rounded_Xsol))
print("\n2. Un número de iteraciones de:",it)
print("\n3. Un error asociado de:",error)