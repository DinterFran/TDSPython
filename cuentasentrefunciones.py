# importar libreriras
import numpy as np
import matplotlib.pyplot as plt
# generar funcion escalon u[n-a]
def unit_step(a, n): #definimos una funcion cuyos parametros son a y n
    unit =[] #genera una lista vacia
    for sample in n: #el sample, que es ? una variable ? empieza en cero?
        if sample<a:
            unit.append(0) #si es menor a "a" pone ceros
        else:
            unit.append(1) #si es mayor o igual a "a" pone unos
    return(unit) # devuelve el valor de la lista

def unit_impulse(a, n): #genero una funcion que depende de los parametros a y n
    delta =[]
    for sample in n:
        if sample == a: # solo si es igual a "a" pone un uno
            delta.append(1)
        else:
            delta.append(0)
             
    return delta #devuelve el valor de la funcion
a = 0
UL = 10
LL = -10
n = np.arange(LL, UL, 1)
escalon = unit_step(a, n)
a = 1
infi = unit_impulse(a,n) # tenemos una lista con un 1 en a
b = [n * 3 for n in infi] #escalamos la lista por 3
diferencia = [e1 - e2 for e1, e2 in zip(escalon,b)] # genero 2 variables e1 y e2, las cuales pertenecen a las listas generadas y resto en mi nueva lista. Zip
plt.stem(n, diferencia)
plt.xlabel('n')
plt.xticks(np.arange(LL, UL, 1))
plt.yticks(np.arange(-3, 3, 1))
plt.ylabel('u[n]')
plt.title('Unit step u[n-a]')
plt.savefig('diferencia.png')
