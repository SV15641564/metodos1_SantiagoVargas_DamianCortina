# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:38:58 2022

@author: damia
"""
import numpy as np
from tqdm import tqdm

def f(x,y,z,a,b,c,d,e):
    return (2**(-7))*(x+y+z+a+b+c+d+e)**2

def GetPoints(min_,max_): 
    x = np.random.uniform(min_,max_)
    y = np.random.uniform(min_,max_)
    z = np.random.uniform(min_,max_)
    a = np.random.uniform(min_,max_)
    b = np.random.uniform(min_,max_)
    c = np.random.uniform(min_,max_)
    d = np.random.uniform(min_,max_)
    e = np.random.uniform(min_,max_)
    return x,y,z,a,b,c,d,e

N = int(1e6/2)
Sample = np.zeros(N)
 
for i in tqdm(range(N)):
    x,y,z,a,b,c,d,e = GetPoints(0,1)
    Sample[i] = f(x,y,z,a,b,c,d,e)
        
Integral = np.average(Sample)
print("\n\nObtenido:     ||Teórico:")
print(str(round(Integral,12))+"||"+str(round(25/192,12)))
print("\nLa diferencia entre ambos valores redondeada al tercer decimal es de:",np.abs(round(Integral - (25/192),3)))
