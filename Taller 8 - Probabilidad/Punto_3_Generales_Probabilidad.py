# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 15:07:21 2022

@author: damia
"""
# =============================================================================
# Punto 3:
# =============================================================================
PC = 0.8
PD = 0.6
PA = 0.5

PCUD = PC + PD - PA

print("\nA) La probabilidad de una suscripción a al menos un servicio está dada por la probabilidad de la unión, P(C U D) =",PCUD)
      
SoloC = PCUD - PD
SoloD = PCUD - PC

print("\nB) La probabilidad de que sea uno o el otro está dado por la suma de la probabilidad entera menos la del total del otro, P(A n Bc) U P(B n Ac) =",SoloC + SoloD)