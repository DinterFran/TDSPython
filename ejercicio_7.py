#ejercicio 7, el resultado por ser un sistema LTI es una resta de dos funciones exponenciales 
#decrecientes atrasadas en 2 y 5
## importar libreriras
import numpy as np
import matplotlib.pyplot as plt
def unit_step(a, n): #definimos una funcion cuyos parametros son a y n
    unit =[] #genera una lista vacia
    for sample in n: #el sample, que es ? una variable ? empieza en cero?
        if sample<a:
            unit.append(0) #si es menor a "a" pone ceros
        else:
            unit.append(1) #si es mayor o igual a "a" pone unos
    return(unit) # devuelve el valor de la lista

n = np.arange(0, 10)
x = np.exp(-0.5*(n - 2))
y = np.exp(-0.5*(n - 5))
a = 2
exp_corrida1 = x*unit_step(a,n)
a = 5
exp_corrida2 = y*unit_step(a,n)
diferencia = [e1 - e2 for e1, e2 in zip(exp_corrida1,exp_corrida2)]
plt.stem(n, diferencia)
plt.xlabel('n')
plt.xticks(np.arange(0, 10, 1))
plt.yticks(np.arange(-3, 3, 1))
plt.ylabel('e[n]')
plt.title('funcion exponencial')
plt.savefig('exponenciales.png')
    