from random import *

#Pide datos por rango
def rangoE1():
    print("\n\n")
    E1 = str(input("Introduzca los simbolos de E1: "))
    E1 = list(E1)
    print("\n\n")
    return E1


#Pide datos uno por uno
def individualE1():
    E1 = list()
    tam = int(input("Tamaño del alfabeto E1: "))
    n = 0

    print("Alfabeto E1...")

    while n < tam:
        E1.append(input("Ingrese los caracteres de E1: "))
        n += 1

    return E1

#Genera el lenguaje l1 de forma aleatorea apartir de E1
def generaLeng1(arg):
    pass

#Genera el lenguaje l2 de forma aleatorea apartir de E1
def generaLeng2(arg):
    pass

#Funcion que pide el tamaño de la palabra y devuelve esa palabra para agregarla a la lista
def tamPalabra(E1):
    tam = int(input("Tamaño de la palabra: "))

    f = str()

    for x in range(tam):
        f = f + choice(E1)

    return f
#Funcion de Union de los lenguajes
def unionL(L1,L2):

    L = list()

    e = 0

    for x in L1:
        for y in L2:
            ##L = x + y
            L.append( x + y)


    print("\n\n\n**UNION***")
    while e < len(L):
        print(L[e])
        e += 1

#Funcion de concatenacion de dos lenguajes
def concatL(L1,L2):
    Lc = L1 + L2
    print("\n\n*****Concatena L1 y L2: \n", Lc ,"*****")



#Funcion: diferencia de dos lenguajes
def diferenciaL(L1,L2):
    #diferencia de L1 y L2:
    print("\n\n******Diferencia******\n\n")

    #Quita los elementos iguales en las mismas listas
    c1 = set(L1)
    c2 = set(L2)

    c11 = c1
    c22 = c2

    #Quita los elementos iguales que puedan estar en l1 y l2
    Ch = c1 - c2

    i = 0

    print("\n\n****LD1 = L1 - L2 = ", Ch ," ****")
    #while i < len(Ld1):
    #    print("Ld1 = ", Ld1[i])
    #    i += 1
    Chh = c22 - c11

    print("\n\n****LD2 = L2 - L1 = ", Chh ," ****")


""" Inicio del programa """



n = 0
m = 0

#Pide datos para sigma(E1) por rango o signo por signo
desea = input("Llenado individual[individual] o por rango[rango]: ")
#Simbolo por simbolo
if desea == "individual":
    E1 = individualE1()

    L1 = list()

    L2 = list()

    i = 0

    j = 0

    t = int(input("\nNumero de palabras de L1: "))

    while i < t:
        p = tamPalabra(E1)
        L1.append(p)
        i += 1

    i = 0

    print("\n\nL1: ")

    while i < len(L1):
        print(L1[i])
        i +=1


    d = int(input("\nNumero de palabras de L2: "))

    while j < d:
        k = tamPalabra(E1)
        L2.append(k)
        j += 1


    print("\n\nL2: ")

    j = 0

    while j < d:
        print(L2[j])
        j += 1

    unionL(L1,L2)
    concatL(L1,L2)
    diferenciaL(L1,L2)

#Por rango***************************************************************************
elif desea == "rango":
    E1 = rangoE1()

    L1 = list()

    L2 = list()

    i = 0

    j = 0

    t = int(input("\nNumero de palabras de L1: "))

    while i < t:
        p = tamPalabra(E1)
        L1.append(p)
        i += 1

    i = 0

    print("\n\nL1: ")

    while i < len(L1):
        print(L1[i])
        i +=1


    d = int(input("\nNumero de palabras de L2: "))

    while j < d:
        k = tamPalabra(E1)
        L2.append(k)
        j += 1


    print("\n\nL2: ")

    j = 0

    while j < d:
        print(L2[j])
        j += 1

    unionL(L1,L2)
    concatL(L1,L2)
    diferenciaL(L1,L2)

else:
    print("Escriba bien...")


#Longitut y np
#print(randrange(10)) random

#Fin del programa
"""
L1 = list()

L2 = list()

i = 0

j = 0

t = int(input("\nNumero de palabras de L1: "))

while i < t:
    p = tamPalabra(E1)
    L1.append(p)
    i += 1

i = 0

print("\n\nL1: ")

while i < len(L1):
    print(L1[i])
    i +=1


d = int(input("\nNumero de palabras de L2: "))

while j < d:
    k = tamPalabra(E1)
    L2.append(k)
    j += 1


print("\n\nL2: ")

j = 0

while j < d:
    print(L2[j])
    j += 1

unionL(L1,L2)
concatL(L1,L2)
diferenciaL(L1,L2)
"""
