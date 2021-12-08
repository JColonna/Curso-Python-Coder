def calcularArea(altura, base):
    area = altura * base
    return(area)

calcularArea(10, 15)

import math
print(math.pi)
def areaCirculo(radio):
    area = (radio ** 2) * math.pi
    return(area)
areaCirculo(5)

def relacion(a, b):
    if a > b:
        return(1)
    if a < b: 
        return(-1)
    if a == b:
        return(0)

def intermedio(a,b):
    medio = (a + b) / 2
    return(medio)
intermedio(-12,24)

def recortar(num, limInf, limSup):
    if num  < limInf:
        return(limInf)
    if num > limSup:
        return(limSup)
    if num > limInf and num < limSup:
        return(num)
recortar(15, 0, 10)

def separar(lista):
    pares = [ ]
    impares = [ ]
    for i,n in lista:
        if i % 2 == 0:
            pares.append(i)
        if i % 2 != 0:
            impares.append(i)
    print(pares)
    print(impares)
separar([6,5,2,1,7])


