from random import randrange, choice

"""
S -> IEF
I -> a
E -> a*|b*
F -> b
"""
#Genera el conjunto
def genera():
	print("\n *** Genera el conjunto... *** ")
	S, I, F, E = "", "a", "b", ""
	conjunto = []
	ra = randrange(23)
	for i in range(ra):
		E = ""
		r = choice(['a', 'b', 'a', 'b'])
		if r == 'a':
			for j in range(ra):
				E += r
		elif r == 'b':
			for k in range(ra):
				E += r
		S = I+E+F
		conjunto.append(S)
		S = ""
	
	print("conjunto=",set(conjunto))

#Manda un mensaje si es aceptada
def compara(S):
	print("*** Nos dice si es aceptada o no... *** ")
	a = ""
	contA = 0
	contB = 0
	t = 0
	if S[0]=='a' and S[len(S)-1]=='b':
		E = list(S[1:len(S)-1])
		t = len(E)
		for e in E:
			if e == 'a':
				contA += 1
			else:
				contB += 1
		if t == contA:
			print("Gramatica aceptada: ", S)
		elif t == contB:
			print("Gramatica aceptada: ", S)
		else:
			print("No aceptado: ", S)
	else:
		print("No es aceptada: ", S)


#Palabra ya definida
#S = "aaaaaaaab"
#Aqui se puede introducir la palabra
S = input("Introduzca una palabra que contenga solo a y b: ")
compara(S)
genera()

"""
i = 0

while i < 10:
	print(randrange(20))
	i += 1
"""