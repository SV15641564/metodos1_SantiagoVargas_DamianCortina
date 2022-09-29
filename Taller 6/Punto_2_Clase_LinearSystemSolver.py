# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 08:55:33 2022

@author: damia
"""
import numpy as np

M = np.array([[3,-1,-1],[-1.,3.,1.],[2,1,4]]) #Se decidió usar el ejemplo de clase, ya que sabemos la solución.
b = np.array([1.,3.,7.])

class LinearSystemSolver:
    
    def __init__(self,A,b):
        self.A = A
        self.b = b
        self.itmax = 1000
        self.error = 1e-10
        
    def Method1(self): #GetJacobiMethod
        M,N = self.A.shape
        x = np.zeros(N)
        sum_k_iteration = np.zeros_like(x)
        x = [0,0,0]
        it = 0
        residue = np.linalg.norm(self.b - np.dot(self.A,x))
        while (residue > self.error and it < self.itmax):
            it += 1
            for i in range(M):
                sum_ = 0
                for j in range(N):
                    if i != j:
                        sum_ += self.A[i][j]*x[j]
                sum_k_iteration[i] = sum_
            for i in range(M):
                if self.A[i,i] != 0:
                    x[i] = (self.b[i] - sum_k_iteration[i])/self.A[i,i]
                else:
                    print('No invertible con Jacobi')
            residue = np.linalg.norm(self.b - np.dot(self.A,x))
        return x,it,residue
        
    def Method2(self): #GetGaußSeidlMethod
        M,N = self.A.shape
        x = np.zeros(N)
        sum_k_iteration = np.zeros_like(x)
        x = [0,0,0]
        it = 0
        residue = np.linalg.norm(self.b - self.A@x)
        while (residue > self.error and it < self.itmax ):
            it += 1
            for i in range(M):
                sum_ = 0
                for j in range(N):
                    if i != j:
                        sum_ += self.A[i][j]*x[j]
                sum_k_iteration[i] = sum_
                x[i] = (self.b[i] - sum_k_iteration[i])/self.A[i,i]
            residue = np.linalg.norm(self.b - self.A@x)
        return x,it,residue

Vector = LinearSystemSolver(M,b)
rounded_Xsol1 = [round(variable,10) for variable in Vector.Method1()[0]]
rounded_Xsol2 = [round(variable,10) for variable in Vector.Method2()[0]]

print("\n1. Usando el método Jacobi en el sistema de ecuaciones aportado se obtuvo un vector solución redondeado al décimo "+\
      "decimal (X,Y,Z) =",tuple(rounded_Xsol1))
print("-Usando el método Gauss-Seidl se obtuvo un vector solución también redondeado al décimo "+\
      "decimal (X,Y,Z) =",tuple(rounded_Xsol2))
    
print("\n\n2. Usando el método Jacobi el sistema se tardó "+str(Vector.Method1()[1])+" iteraciones.")
print("-Usando el método Gauss-Seidl "+str(Vector.Method2()[1])+" iteraciones.")

print("\n\n3. Existe un error asociado al método Jacobi de:",Vector.Method1()[2])
print("-En el método Gauss-Seidl es de:",Vector.Method2()[2])