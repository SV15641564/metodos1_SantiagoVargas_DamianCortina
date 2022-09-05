# -*- coding: utf-8 -*-

def factorial(numero: int)->int:
    factorial=1
    for i in range (1, numero + 1):
        factorial = factorial * i
    return factorial

def variacion_sr(n: int, r:int)->int:
    
    iniciar=True
    while iniciar:    
        if n>r:
            variacion=factorial(n)/factorial(n-r)
            return int(variacion)
            iniciar=False
        else:
            n=int(input("Ingrese un valor para n tal que n>r: "))
            r=int(input("Ingrese un valor para r tal que n>r: "))
    

def combinaciones_sr(n:int, m:int)->int:
    
    iniciar=True
    while iniciar:
    
        if n>m:
            fact_n_m=factorial(n-m)
            fact_m=factorial(m)
            fact_n=factorial(n)
            combinacion=fact_n/(fact_m*fact_n_m)
            
            return int(combinacion)
            iniciar=False
        else:
            n=int(input("Ingrese un valor para n tal que n>m: "))
            m=int(input("Ingrese un valor para m tal que n>m: "))
    
