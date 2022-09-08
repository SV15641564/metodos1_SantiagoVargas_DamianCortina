# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 20:14:17 2022

@author: damia
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sym
import os.path as path
import wget
import math #Solo para la función asin
file = 'C:/Users/damia/OneDrive/Documentos/Parabolico.csv'
url = 'https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Parabolico.csv'
if not path.exists(file):
    Path_ = wget.download(url,file)
else:
    Path_ = file

Data = pd.read_csv(Path_,sep=',')

X = np.float64(Data['X'])
Y = np.float64(Data['Y'])

h = 0.0001

def Lagrange(x,xi,j):
    
    prod = 1.0
    n = len(xi)
    
    for i in range(n):
        if i != j:
            prod *= (x - xi[i])/(xi[j]-xi[i])
            
    return prod
def Poly(x,xi,yi):
    
    Sum = 0.
    n = len(xi)
        
    for j in range(n):
        Sum += yi[j]*Lagrange(x,xi,j)
        
    return Sum

x = np.linspace(0,7,100)
y = Poly(x,X,Y)



xsym = sym.Symbol('x')
f = Poly(xsym,X,Y)
f = f.expand()


def derivada(f,x):
  return (f.subs(xsym,x+h)-f.subs(xsym,x-h))/(2*h)



def GetNewtonMethod(f,df,xn,itmax=1000,precision=1e-5):
    error = 1
    it = 0
    while error > precision and it < itmax: 
        try:
            xn1 = xn - f.subs(xsym,xn)/df(f,xn)
            error = np.abs(f.subs(xsym,xn)/df(f,xn))
        except ZeroDivisionError:
            print('Hay un error de división por cero.')     
        xn = xn1
        it += 1
    if it == itmax:
        return False
    else:
        return xn


def GetAllRoots(x,tolerancia=8):
    Roots = np.array([])
    for i in x:
        root = GetNewtonMethod(f,derivada,i)
        if root != False:
            croot = round(root,tolerancia)
            if round(croot,2) not in Roots:
                if np.abs(croot) < 0.001:
                    Roots = np.append(Roots,round(croot,8))
                else:   
                    Roots = np.append(Roots,round(croot,8))
                    
    Roots.sort()
    return Roots


espacio_x = np.linspace(-1,100,30)
Roots = GetAllRoots(espacio_x)


resultado = []
for i in Roots:
    if i not in resultado:
        resultado.append(i)
        
print("1. Los ceros del polinomio indicado son:",resultado,"\n")
print("2. Por ende, sabemos que la ecuación de rango R = (v_0^2*sen(2θ))/g va a valer:",round(resultado[1],3),"pues esta es una función cuadrática.\n")
print("3. De la función de movimiento parabólico Vy = V_0y^2 + 2g(Y-Y_0) sacaremos V_0y.","\n")
print("4. Tomamos el punto máximo de la parábola para que Vy y Y_0 valgan 0 y Y sea igual a Y_max.","\n")
print("5. Y hallamos el Y_max haciendo un for-loop por los valores de Y de la parábola y que nos devuelva el mayor. (veáse esto abajo de este print en el código)","\n")

mayor = 0

for i in y:
    if i > mayor:
        mayor = i

print("6. Ya habiendo hallado Y_max ("+str(round(mayor,3))+") se procede a calcular V_0y de la manera antes dicha en la línea 3.","\n")

V_0y = np.sqrt(2*(9.8)*mayor)
print("7. Esto nos da un V_0y de",round(V_0y,3),"Para continuar se sabe que dado a las características de la ecuación calculada del polinomio, el coeficiente que acompaña a la x es igual a V_0y/V_0x.\n")    
print("8. Se iguala V_0y/V_0x al coeficiente obtenido. Lo que da 3,4202/V_0x = 0.36397 y de aquí se despeja V_0x\n")

V_0x = V_0y/0.363970234266202
print("V_0x daría un total de",round(V_0x,3),"Mediante pitágoras se calcula la velocidad inicial: V_0 = sqrt(V_0x^2 + V_0y^2)\n")

V_0 = np.sqrt(V_0x**2+V_0y**2)
print("9. Esto nos daría que V_0 es igual a:",round(V_0,4),"lo cual es casi 10.\n")
print("10. Para hallar el ángulo se despeja de la ecuación de rango indicada en la segunda línea de este mensaje.\n")
print("11. El ángulo θ será igual a (math.asin((R*(g))/(V_0**2)))/2\n")

ang_rad = (math.asin((resultado[1]*(-9.8))/(V_0**2)))/2
ang_grados = np.abs((ang_rad*180)/np.pi)
print("12. Esto nos da un θ de: "+str(round(ang_grados,4))+"° que es casi 20° exactos.\n")
print("13. V_0 = "+str(V_0)+"\n      θ = "+str(ang_grados))

plt.scatter(X,Y,color='c')
plt.plot(x,y,color='tab:grey')