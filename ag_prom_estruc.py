# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:21:34 2020

@author: 15-db0011
"""

import numpy as np
import math as mat

def Rastrigin(matriz):  
    Resultado=np.zeros((fila,1))
    for i in range(fila):
        acum=0
        suma=0
        for j in range(columna):
            acum=((matriz[i,j]**2)-(10*mat.cos(2*mat.pi*matriz[i,j])))+acum
        suma=(10*columna)+acum
        Resultado[i]=suma
    return Resultado
    
def valor(vector):
    menor = vector[0]

    for i in (range(0, len(vector))):
      
        if vector[i]<menor:
            menor = vector[i]
    return menor

def Seleccion(matriz):
    a=Rastrigin(matriz)
    b=np.zeros((fila,columna))
   
    for i in range(fila):
        na1=np.random.randint(0,fila)
        na2=np.random.randint(0,fila)
        
        while na1==na2: 
            na1=np.random.randint(0,fila)
            na2=np.random.randint(0,fila)
        print(na1,na2)
        fila1=a[na1]
        fila2=a[na2]
        if fila1<fila2:
            b[i]=matriz[na1]
        else:
            b[i]=matriz[na2]
    return b    

def cruce(matriz):
    print(matriz) 
    w=np.zeros((fila,columna))
    acum=0
    for i in range(fila//2):
        na1=np.random.randint(columna)
        print(na1)
        if na1<=pc:
            w[acum]=np.concatenate((matriz[acum,:na1],matriz[acum+1,na1:]),axis=0)
            w[acum+1]=np.concatenate((matriz[acum+1,:na1],matriz[acum,na1:]),axis=0)
            acum=(i*2)+2
        else:
             matriz=matriz
    return w

def mutacion(matriz):
    a=-5.12
    b=5.12
    for i in range(fila):
        na1=np.random.rand()
        na=np.random.randint(columna)
        print(na1)
        if na1<pm:
            matriz[i,na]=a+(b-a)*np.random.rand()
        else:
            matriz[i]=matriz[i]
    return(matriz)  
print("Inicia programa principal")
x=4
y=3
z=int(input("Diga el numero de iteraciones"))
pc=0.90
pm=0.075

"Parametro de la matriz:"
a=-5.12
b=5.12
vector = []
Mejorx = 0 
matriz=a+(b-a)*np.random.rand(x,y)
"Redinmensionamiento"
fila,columna=matriz.shape

for i in range (z):
    print(matriz)
    vector = (Rastrigin(matriz))
    print("Vector Rastrigin")
    print(vector)
    Mejorx=(valor(vector))
    print('')
    print("El mejor de f(x) es: " + str (Mejorx))
    print('')
    Padres=(Seleccion(matriz))
    print('')
    print("Esta es la matriz de padres:")
    print('')
    print((Padres))
    print('')
    Hijos=(cruce(matriz))
    print("Los hijos son: ")
    print('')
    print(Hijos)
    print('')
    Hijos2 = mutacion(matriz)
    print('')
    print("Los hijos mutados son: ")
    print('')
    print(Hijos2)


