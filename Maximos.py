1# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 07:19:12 2022

@author: damia
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

url='https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/EstrellaEspectro.txt'

df = pd.read_csv(url)

df = pd.read_csv(url,header=None,sep="  ")

plt.plot(df[0],df[1])

lista = argrelextrema(np.array(list(df[1])), np.greater)
ls = lista[0].tolist()

lista_max = []
lista_max_0=[]
pasos = 0
while pasos < (len(ls)):
    
        lista_max.append(df[1][ls[pasos]])
        lista_max_0.append(df[0][ls[pasos]])
        pasos += 1
    
plt.scatter(lista_max_0,lista_max)



