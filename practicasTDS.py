#append sirve para agregar un elemnto a la lista
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
# graficar un escalon u[n-a]
a = 2 # Enter retraso / adelanto
UL = 10 #rango superior
LL = -10 #rango inferior
n = np.arange(LL, UL, 1)
unit = unit_step(a, n)
plt.stem(n, unit)
plt.xlabel('n')
plt.xticks(np.arange(LL, UL, 1))
plt.yticks([0, 1])
plt.ylabel('u[n]')
plt.title('Unit step u[n-a]')
plt.savefig('UnitStep.png')
# Funcion delta d(a)
def unit_impulse(a, n): #genero una funcion que depende de los parametros a y n
    delta =[]
    for sample in n:
        if sample == a: # solo si es igual a "a" pone un uno
            delta.append(1)
        else:
            delta.append(0)
             
    return delta #devuelve el valor de la funcion
a = 4 # Enter delay or advance
UL = 10
LL = -10
n = np.arange(LL, UL, 1)
d = unit_impulse(a, n)
plt.stem(n, d)
plt.xlabel('n')
plt.xticks(np.arange(LL, UL, 1))
plt.yticks([0, 1])
plt.ylabel('d[n]')
plt.title('Unit Impulse d[4]')
plt.savefig("UnitImpulse.png")
# Funcion rampa r(n)
# r(n)= n for n>= 0, r(n)= 0 otherwise
def unit_ramp(n):
    ramp =[]
    for sample in n:
        if sample<0:
            ramp.append(0)
        else:
            ramp.append(sample) 
    return ramp
 
UL = 10
LL = -10
n = np.arange(LL, UL, 1)
r = unit_ramp(n)
plt.stem(n, r)
plt.xlabel('n')
plt.xticks(np.arange(LL, UL, 1))
plt.yticks([0, UL, 1])
plt.ylabel('r[n]')
plt.title('Unit Ramp r[n]')
plt.savefig("UnitRamp.png")
 
# Funcion exponencial signals e**(at)
def exponential(a, n):
    expo =[]
    for sample in n:
        expo.append(np.exp(a * sample))
    return (expo)
        
a = 2
UL = 10
LL = -10
n = np.arange(LL, UL, 1)
x = exponential(a, n)
plt.stem(n, x)
plt.xlabel('n')
plt.xticks(np.arange(LL, UL, 1))
# plt.yticks([0, UL, 1])
plt.ylabel('x[n]')
plt.title('Exponential Signal e**(an)')
plt.savefig("Exponential.png")