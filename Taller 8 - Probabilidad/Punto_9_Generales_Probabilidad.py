# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 16:14:54 2022

@author: damia
"""
# =============================================================================
# Punto 9:
# =============================================================================
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from tqdm import tqdm

N = int(1.5e5)
ncoins = 4
events = [-1,1]
Sample = np.zeros((N,ncoins))

def GetProb(p11,p12):  
    for i in range(N):
        
        exp1 = np.random.choice(events,p=[1-p11,p11])
        Sample[i,0] = exp1
        
        exp2 = np.random.choice(events,p=[1-p12,p12])
        Sample[i,1] = exp2
        
        exp3 = np.random.choice(events)
        Sample[i,2] = exp3
        
        exp4 = np.random.choice(events)
        Sample[i,3] = exp4
        
    Events = 0
    
    for i in range(len(Sample)):
        NCaras = 0
        for j in range(ncoins):
            if Sample[i][j] == 1:
                NCaras += 1
        if NCaras == 2:
            Events += 1
    return Events/N

num = int(20)
Results = np.zeros((num,2))

for i in tqdm(range(num)):
    p12 = np.linspace(0.1,0.5,num)
    p11 = np.linspace(0.1,0.9,num) 
    Results[i,0] = p11[i]
    Results[i,1] = p12[i]

P11,P12 = np.meshgrid(Results[:,0],Results[:,1])
Z = np.empty_like(P11)

for i in tqdm(range(len(Z))):
    for j in tqdm(range(len(Z[0]))):
        Z[i,j] = GetProb(P11[i,j],P12[i,j])

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1, 1, 1, projection='3d')        
ax.plot_surface(P11,P12,Z,cmap=cm.coolwarm)
ax.view_init(45,85)