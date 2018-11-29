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

#Funcion que pide el tamaño de la palabra y devuelve esa palabra para agregarla a la lista
def tamPalabra(E1,palabras):
    #tam = int(input("Tamaño de la palabra: "))

    f = str()

    for x in range(palabras):
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


    print("\n\n\n**Concatenacion***")
    while e < len(L):
        print(L[e])
        e += 1

#Funcion de concatenacion de dos lenguajes
def concatL(L1,L2):
    Lc = L1 + L2
    print("\n\n*****Union L1 y L2: \n", Lc ,"*****")



#Funcion: diferencia de dos lenguajes
def diferenciaL(L1,L2):#asignar l1 y l2 a otras listas(pero las copias de estas L1[:]) ej: Li = L1 etc, hacer lo mismo con las otras funciones
    #diferencia de L1 y L2:

    print("\n\n******Diferencia******\n\n")

    n = 0

    m = 0

    Ld = []

    Ldd = []

    print("L1 - L2: ")

    while n < len(L1):
        while m < len(L2):
            if L1[n] == L2[m]:
                print(L1[n])
                print(L2[m])
            else:

                Ld.append(L1[n])
            m += 1
        n += 1

    print(Ldd)
    print(Ld)
    print("\n\nL2-L1: ")

    """

    n = 0

    m = 0

    while n < len(L2):
        while m < len(L1):
            if L2[n] != L1[m]:
                Ldd.append(L2[n])
            n += 1
        m += 1
    print(Ldd)"""

#Funcion de potencia de un lenguaje
def potenciaL(L1,L2):

    print("*******Potencia********")

    lengua = input("Que lenguaje desea L1 o L2: ")

    pote = int(input("A que potencias (-5 a 5): "))

    ele1 = []

    if pote >= -5 and pote < 0:
        #Si es par
        if pote%2 == 0:
            if lengua == "l1" or lengua == "L1":
                n = 0
                print("Potencia de L1: ", n)
                while n < len(L1):
                    print(L1[n])
                    n += 1
            else:
                n = 0
                print("Potencia de L2: ", n)
                while n < len(L2):
                    print(L2[n])
                    n += 1
        #No es par
        else:
            if lengua == "l1" or lengua == "L1":
                n = 0
                while n < len(L1):
                    cad = ""
                    cad = L1[n]
                    ele1.append(cad[::-1])
                    n += 1
                print(ele1)
            else:
                n = 0
                while n < len(L2):
                    cad = ""
                    cad = L2[n]
                    ele1.append(cad[::-1])
                    n += 1
                print(ele1)

    elif pote <= 5 and pote >= 0:
        if lengua == "l1" or lengua == "L1":
            print("Potencia de L1: ",L1 * pote)
        else:
            print("Potencia de L2: ",L2 * pote)
    else:
        print("Escribiste: ", pote, " no es correcto...")


""" *********************Inicio del programa********************************* """



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

    t = int(input("\nNumero de palabras de L1 y L2: "))
    palabras = int(input("\nTamaño de las palabras: "))

    while i < t:
        p = tamPalabra(E1,palabras)
        L1.append(p)
        i += 1

    i = 0

    print("\n\nL1: ")

    while i < len(L1):
        print(L1[i])
        i +=1


    #d = int(input("\nNumero de palabras de L2: "))

    while j < t:#d
        k = tamPalabra(E1,palabras)
        L2.append(k)
        j += 1


    print("\n\nL2: ")

    j = 0

    while j < t:
        print(L2[j])
        j += 1

    unionL(L1[:],L2[:])#unionL(L1[:],L2[:])--> solo se envian las copias
    concatL(L1[:],L2[:])
    diferenciaL(L1[:],L2[:])
    potenciaL(L1[:],L2[:])

#Por rango***************************************************************************
elif desea == "rango":
    E1 = rangoE1()

    L1 = list()

    L2 = list()

    i = 0

    j = 0

    t = int(input("\nNumero de palabras de L1 y L2: "))
    palabras = int(input("\nTamaño de la palabra: "))

    while i < t:
        p = tamPalabra(E1,palabras)
        L1.append(p)
        i += 1

    i = 0

    print("\n\nL1: ")

    while i < len(L1):
        print(L1[i])
        i +=1


    #d = int(input("\nNumero de palabras de L2: "))

    while j < t:#d
        k = tamPalabra(E1,palabras)
        L2.append(k)
        j += 1


    print("\n\nL2: ")

    j = 0

    while j < t:#d
        print(L2[j])
        j += 1

    unionL(L1[:],L2[:])#unionL(L1[:],L2[:])--> solo se envian las copias
    concatL(L1[:],L2[:])
    diferenciaL(L1[:],L2[:])
    potenciaL(L1[:],L2[:])

else:
    print("Escriba bien...")


""" *********Fin del programa ******* """
