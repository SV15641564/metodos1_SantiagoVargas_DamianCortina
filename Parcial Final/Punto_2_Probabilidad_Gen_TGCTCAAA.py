# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 11:07:01 2022

@author: damia
"""
import numpy as np

π = np.array([0.25,0,0.5,0.25])
T = np.array([[0.4,0.2,0.2,0.2],[0.25,0.25,0.25,0.25],[0.3,0.3,0.1,0.3],[0.1,0.1,0.1,0.7]])

Theorical_Result = 0.25*0.1*0.3*0.25*0.1*0.25*0.4**2

Dict = {0:'A',1:'C',2:'G',3:'T'}

text = 'TGCTCAAA'

for i in range(len(Dict)):
    if Dict[i] == text[i]:
        index = i
 
probability =  π[index]      
row_index = [] 
column_index = []

for j in range(len(text)):
    for i in range(len(Dict)):
        if Dict[i] == text[j]:
            row_index.append(i)
            column_index.append(i)
            
row_index.remove(row_index[-1])            
column_index.remove(column_index[0])
        
for i in range(len(row_index)):
    probability *= T[row_index[i],column_index[i]]
    
print("Probabilidad calculada:","||","Probabilidad teórica:")   
print(probability,"  ||",Theorical_Result)