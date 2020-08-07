# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:12:34 2020

@author: 15-db0011
"""

import numpy as  np

def Pob_ini(tpob,c):
    Pob=np.zeros((tpob,c))
    for i in range(tpob):
        for j in range(c):
            tmp=np.random.permutation(c)+1
            #print(tmp)
            Pob[i,:]=tmp
            #print(Pob) 
    return Pob
        
def decod2(a,c,tpob):
    matriz=np.zeros((tpob,(c*2)+1))
    matriz=matriz.astype(int)
    tmp=0
    q=25
    #Nodo y Primer cliente
    for i in range(tpob):
            matriz[i,1]=a[i,0]
    #Del segundo cliente en adelante
    for i in range(tpob):
            tmp=Dmd1[a[i,0]-1]
            pos=1
            j=1
            while j<c:
                tmp=tmp+Dmd1[a[i,j]-1]
                if tmp<=q:
                    matriz[i,pos+1]=a[i,j]
                    pos=pos+1
                    j=j+1
                else:
                    matriz[i,pos+1]=0
                    pos=pos+1
                    tmp=0
    return matriz

def costo(b,c,tpob,Dmd1):
    arco=np.array([[0,1,2,1,1,2],[1,0,1,1,2,2],
                   [1,1,0,1,2,1],[1,2,2,0,1,1]
                   ,[2,1,1,2,0,2],[1,2,1,1,2,0]])
    print(' ')
    print(arco)
    valor=np.zeros((fila,1))
    for i in range(fila):
        cont=0
        for j in range(columna):
            cont= cont+arco[b[i,j],b[i,j-1]]
            valor[i,0]=cont
    return valor

def valor(d,c,a):
    menor = d[0]
    sol=np.zeros((c))
    posic=0
    for i in (range(0, len(d))):
        if d[i]<menor:
            menor = d[i]
            posic=i
            sol[:]=a[posic,:]
    return menor,sol

def seleccion(b,d):
    padres=np.zeros((tpob,c))
    for i in range(tpob):
        a1=np.random.randint(0,tpob)
        a2=np.random.randint(0,tpob)
       
        while a1==a2:
            a1=np.random.randint(0,tpob)
            a2=np.random.randint(0,tpob)    
#        print(a1,a2)

        if d[a1]<=d[a2]:
            padres[i,:]=a[a1,:]
        else:
            padres[i,:]=a[a2,:]
    return padres

def cruce(papas,tpob,c):
    hj=np.zeros((tpob,c))
    hj=hj.astype(int)
    for i in range(0,tpob,2):
        na1=np.random.rand()
#        print('N° aleatorio es: '+ str (na1))
        if na1<=pc:
#            print('Se cruza')
            for j in range(c):
                if papas[i,j] == papas[i+1,j]:
                    hj[i,j]=papas[i,j]
                    hj[i+1,j]=papas[i+1,j]
#                    print(hj)           
        nac=np.random.randint(0, c-1)
#        print('El punto de corte es: ' +str (nac))
        m=papas[i,0:nac+1]
        n=papas[i+1,0:nac+1]
        hj[i,0:nac+1]=m
        hj[i+1,0:nac+1]=n

    return hj

def fill(hijos,papas,tpob,c):
    for i in range(0,tpob,2):
        for j in range(c):
            temp=np.where(hijos[i]==papas[i,j])
            temp1=np.where(hijos[i+1]==papas[i+1,j])
#            print(10*'++')
#            print(temp)
#            print(temp1)
            if temp[0].size<=0 and temp1[0].size<=0:
                cc=np.where(hijos[i]==0)
                cc1=np.where(hijos[i+1]==0)
#                print(10*'-')
#                print(cc)
#                print(cc1)
                hijos[i,cc[0][0]]=papas[i,j]
                hijos[i+1,cc1[0][0]]=papas[i+1,j]
#    print(hijos)
    return hijos
def mutacion(hijos, tpob, c):
    c1=0
    c2=0
    for i in range(tpob):
                a1=np.random.randint(0,tpob-1)
                a2=np.random.randint(0,tpob-1)
#                print('# aleatoreos')
#                print(a1,a2)
                while a1==a2:
                    a1=np.random.randint(0,tpob-1)
                    a2=np.random.randint(0,tpob-1)
#                    print('# aleatoreos')
#                    print(a1,a2)
                c1=hijos[i,a1]
                c2=hijos[i,a2]
#                print(c1)
#                print(c2)
                hijos[i,a1]=c2
                hijos[i,a2]=c1
#                print(hijos)   
    return hijos
 
print("Inicia programa Principal")
#tpob=int(input("Digite la cantidad de soluciones: "))
#y=int(input("Ingrese el numero de clientes: "))
tpob=4
c=5
q=25
pc=0.95
Dmd=np.random.randint(1,5,size=(1,tpob))
print(Dmd)
Dmd1=[5,7,10,9,11]
a= Pob_ini(tpob, c)    
a=a.astype(int)
print(' ')
print('Matriz de Clientes')
print(a)
print(' ')
b=decod2(a,c,tpob)
b=b.astype(int)
fila,columna=b.shape
print('    ----- RUTAS -----')
print(b)
d=costo(b,c,tpob,Dmd1)
d=d.astype(int)
print(' ')
print('Costos')
print(d)
e=seleccion(b,d)
e=e.astype(int)
papas=e
print(' ')
print('Padres')
print(papas)
f=cruce(papas,tpob,c)
hijos=f
#print(hijos)
cruce=fill(hijos,papas,tpob,c)
print(' ')
print('Hijos cruce')
print(cruce)
m=mutacion(hijos, tpob, c)
print(' ')
print('Hijos Mutacion')
print(m)
decod22=decod2(m,c,tpob)
print(' ')
print('    ----- RUTAS -----')
print(decod22)
costo2=costo(decod22,c,tpob,Dmd1)
costo2=costo2.astype(int)
print(' ')
print('Costos')
print(costo2)

