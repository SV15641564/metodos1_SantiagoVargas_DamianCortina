#!/usr/bin/env python
# coding: utf-8

# In[35]:


import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(0.1,1.1,101)
h = X[1]-X[0]


# In[68]:


function = lambda x: np.sqrt(np.tan(x))

def derivativePro(f,x):
    return (1/(6*h))*(-8*f(x)+9*f(x+h)-f(x+3*h))


# In[69]:


ansPro = derivativePro(function,X)


# In[70]:


plt.scatter(X,ansPro,color='b')


# In[ ]:

def derivativeCen(f,x):
    return (1/(2*h))*(-3*f(x)+4*f(x+h)-f(x+2*h))

ansCen = derivativeCen(function,X)

plt.scatter(X,ansCen,color='k')





# In[ ]:
dev = lambda x: (1/(np.cos(x)**2))/(2*function(x))

errorPro = dev(X) - ansPro
errorCen = dev(X) - ansCen

plt.scatter(X,errorCen,color='r')
plt.scatter(X,errorPro,color='b')
# In[ ]:
listapro = 0
for i in errorPro:
    listapro += i
listapro /= len(errorPro)

listacen = 0
for i in errorCen:
    listacen +=i 
listacen /= len(errorCen)

print("Se verifica que ambas gráficas de la central y progresiva son muy parecidas (ver plot), y que cuentan con un error promedio por punto de: "+str(listacen)+" y "+str(listapro)+" respectivamente.")
print("\n\nLos errores de ambas dan en igual orden: 10^4: 0.0006 y 0.0004")