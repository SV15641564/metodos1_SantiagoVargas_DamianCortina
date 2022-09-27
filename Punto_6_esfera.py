# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 12:01:59 2022

@author: damia
"""
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

def CreateSphere(N,R):   
    X = np.zeros(N)
    Y = np.zeros_like(X)
    Z = np.zeros_like(X)    
    for i in tqdm(range(N)):  
        u = np.random.rand()
        v = np.random.rand()
        theta = 2*np.pi*u
        phi = np.math.acos((2*v)-1)
        X[i] = R*np.cos(theta)*np.sin(phi)
        Y[i] = R*np.sin(phi)*np.sin(theta)
        Z[i] = R*np.cos(phi)
    return X,Y,Z

X,Y,Z = CreateSphere(10000,1)
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1, projection = '3d')
ax.set_xlim3d(-1,1)
ax.set_ylim3d(-1,1)
ax.set_zlim3d(-1,1)
ax.view_init(22,22)
ax.scatter(X,Y,Z,color='c')

def f(x,y,z,theta):
    return np.sin(theta)*np.exp(np.sqrt(x**2+y**2+z**2))

def GetPoints(thetamin,thetamax,phimin,phimax,R): 
    u = np.random.rand()
    R_ = R*u**(1/4)
    theta = np.random.uniform(thetamin,thetamax)
    phi = np.random.uniform(phimin,phimax)
    x = R_*np.cos(theta)*np.sin(phi)
    y = R_*np.sin(phi)*np.sin(theta)
    z = R_*np.cos(phi)
    return x,y,z,theta

N = int(1e4)
Sample = np.zeros(N)
    
for i in range(N):
    x,y,z,theta = GetPoints(0,np.pi,0,2*np.pi,1)
    Sample[i] = f(x,y,z,theta)
        
Integral = 2*np.pi*np.average(Sample)
print("\nObtenido:        ||Teórico:")
print(str(Integral)+"||"+str(4*np.pi*(np.e-2)))
print("\nLa diferencia entre ambos valores es de:",np.abs(round(Integral - (4*np.pi*(np.e-2)),6)))