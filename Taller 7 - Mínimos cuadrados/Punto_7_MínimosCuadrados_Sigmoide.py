# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 09:57:28 2022

@author: damia
"""
from tqdm import tqdm
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
h = 1e-6


# =============================================================================
# Punto A:
# =============================================================================
x = np.linspace(min(X),max(X),500)

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
def gradiente_descendiente(punto,lr,itmax):
    for i in tqdm(range(int(itmax))):
        x_grad = grad_loss(X,Y, punto[0], punto[1], punto[2])
        punto = punto - (lr*x_grad)
    return punto


# =============================================================================
# Punto E:
# =============================================================================
θ_0 = np.array([1,1,1])
param = gradiente_descendiente(θ_0,5e-4,1e4)

P0 = param[0]
P1 = param[1]
P2 = param[2]

ChiSquared = loss(X,Y,P0,P1,P2)

print("\nE.1) Los parámetros θ_0, θ_1 y θ_2 que mejor se ajusten a los datos del sigmoide generado por el raw son:\n\n"+str(P0)+"\n"+str(P1)+"\n"+str(P2))
print("\n\nE.2) Valor para χ^2 de:",ChiSquared)

# =============================================================================
# Punto F:
# =============================================================================
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(1,1,1)
ax.scatter(X,Y,c='k',label='Scatter Plot')
plt.plot(x,sigmoid(x,P0,P1,P2),c='c',label='Sigmoid Function')