# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 15:58:00 2022

@author: damia
"""
# =============================================================================
# Punto 8:
# =============================================================================
import numpy as np
from tqdm import tqdm 

N = int(1e5)
ncoins = 4
events = [-1,1]
Sample = np.zeros((N,ncoins))

for i in tqdm(range(N)):
    exp = np.random.choice(events, ncoins)
    Sample[i] = exp
    
Events = 0

for i in range(len(Sample)):
    NCaras = 0
    for j in range(ncoins):
        if Sample[i][j] == 1:
            NCaras += 1
    if NCaras == 2:
        Events += 1
        
print("\nResultado:\n"+str(Events/N),"|",3/8)