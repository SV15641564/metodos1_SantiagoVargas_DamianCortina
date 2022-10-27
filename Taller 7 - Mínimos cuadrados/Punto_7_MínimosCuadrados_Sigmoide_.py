# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 09:57:28 2022

@author: damia
"""
from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os.path as path
import wget
file = 'C:/Users/damia/OneDrive/Documentos/Punto_7_MínimosCuadrados.csv'
url = 'https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Sigmoid.csv'
if not path.exists(file):
    Path_ = wget.download(url,file)
else:
    Path_ = file
Data = pd.read_csv(Path_,sep=',')
X = np.float64(Data['x'])
Y = np.float64(Data['y'])
N = Y.size
h = 0.01
print("El programa puede tardar unos segundos. Generalmente menos de 30 segundos...\n\n")


# =============================================================================
# Punto A:
# =============================================================================
def sigmoid(x,P0,P1,P2):
    sigmoid = P0/(P1+np.exp(-P2*x))
    return sigmoid


# =============================================================================
# Punto B:
# =============================================================================
def loss(X, Y, a, b, c):
  ChiSquared = 0
  for i in range(N):
      ChiSquared += (Y[i] - sigmoid(X[i],a,b,c))**2  
  return ChiSquared


# =============================================================================
# Punto C:
# =============================================================================
def grad_loss(x, y, a, b, c):  
  grad = np.zeros(3)
  grad[0] = (loss(X,Y,a+h,b,c)-loss(X,Y,a-h,b,c))/(2*h)
  grad[1] = (loss(X,Y,a,b+h,c)-loss(X,Y,a,b-h,c))/(2*h)
  grad[2] = (loss(X,Y,a,b,c+h)-loss(X,Y,a,b,c-h))/(2*h)
  return grad

  
# =============================================================================
# Punto D:
# =============================================================================
def gradiente_descendiente(punto,lr,itmax,error):
    it = 0
    distancia_al_optimo = 1
    while distancia_al_optimo > float(error) and it < int(itmax):
            x_grad = grad_loss(X,Y, punto[0], punto[1], punto[2])
            punto = punto - lr*x_grad
            distancia_al_optimo = np.linalg.norm(punto - optimize.curve_fit(sigmoid,X,Y)[0])
            it += 1
            if itmax%it == 2000:
                print("Iteración:"+str(it)+"/"+str(int(itmax)))
    return punto, distancia_al_optimo,it


# =============================================================================
# Punto E:
# =============================================================================
θ_0 = np.array([1,1,1])
param = gradiente_descendiente(θ_0,5e-4,2e4,1e-2)

P0 = param[0][0]
P1 = param[0][1]
P2 = param[0][2]

ChiSquared = loss(X,Y,P0,P1,P2)

print("\n\nE.1) Los parámetros θ_0, θ_1 y θ_2 que mejor se ajusten a los datos del sigmoide generado por el raw son:\n\n"+str(P0)+"\n"+str(P1)+"\n"+str(P2))
print("\n\nE.2) Valor para χ^2 de:",ChiSquared)
print("\n\nE.3) Con un error absoluto de ϵ =",param[1])
print("\n\nE.4) Con un número de iteraciones totales de:",param[2])


# =============================================================================
# Punto F:
# =============================================================================
x = np.linspace(min(X),max(X),500)
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(1,1,1)
ax.scatter(X,Y,c='k',label='Scatter Plot')
plt.plot(x,sigmoid(x,P0,P1,P2),c='c',label='Sigmoid Function')