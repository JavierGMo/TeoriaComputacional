def compara(E1,w1,w2):
    n = 0
    m = 0

    while n < len(E1):
        while m < len(E1):
            if w1[n] == E1[m]:
                    w1.pop(n)
            else:
                print("La cadena w1 no es valida....")
                break
            m += 1
        n += 1
    print("Es valida...")

def volverallenar():
    pass

def rangoE1():
    print("\n\n")
    E1 = str(input("Introduzca los simbolos de E1: "))
    E1 = list(E1)
    print("\n\n")
    return E1
    """n = 0
    m = 0
    while n < len(E1):
        print(E1[n])
        n += 1"""

def rangoE2():
    E2 = str(input("Introduzca los simbolos de E2: "))
    E2 = list(E2)
    print("\n\n")
    return E2


def individualE1():
    E1 = list()
    tam = int(input("Tamaño del alfabeto E1: "))
    n = 0

    print("Alfabeto E1...")

    while n < tam:
        E1.append(input("Ingrese los caracteres de E1: "))
        n += 1

    return E1

def individualE2():
    E2 = list()
    tam = int(input("Tamaño del alfabeto E2: "))
    m = 0

    print("\nAlfabeto E2...")

    while m < tam:
        E2.append(input("Ingrese los caracteres de E2: "))
        m += 1


    return E2

E1 = list()
""""
por rangos
E1 = str(input())
E1 = list(E1)
"""
E2 = list()
w1 = list()
w2 = list()

n = 0
m = 0

desea = input("Llenado individual[individual] o por rango[rango]")
if desea == "individual":
    E1 = individualE1()
    E2 = individualE2()

elif desea == "rango":
    E1 = rangoE1()
    E2 = rangoE2()
else:
    print("Escriba bien...")





n = 0
m = 0

print("\n\n")

while n < len(E1):
    w1.append(input("Ingrese w1: "))
    n += 1

print("\n\n")

while m < len(E1):
    w2.append(input("Ingrese w2: "))
    m += 1



compara(E1,w1,w2)
#ingresacadenas(E1,w1,w2)
