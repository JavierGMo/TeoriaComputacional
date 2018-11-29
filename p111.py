def q1(alfabeto):
	for x in alfabeto:
		if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9':
			alfabeto.remove(x)
			print(alfabeto)
			q1(alfabeto)
		elif x == '.':
			alfabeto.remove(x)
			print(alfabeto)
			q2(alfabeto)
		elif x == 'E':
			alfabeto.remove(x)
			print(alfabeto)
			q4(alfabeto)
		else:
			print("No aceptado... ",x)
			break

def q2(alfabeto):
	for x in alfabeto:
		if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9':
			#Ealfabeto.remove(x)
			print(alfabeto)
			q3(alfabeto,x)
		else:
			print("No aceptado... ",x)
			break

def q3(alfabeto,y):
	alfabeto.remove(y)
	if len(alfabeto) == 0:
		print("Esta en el estado de aceptacion q3...\n",alfabeto)
	else:
		for x in alfabeto:
			if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9':
				#alfabeto.remove(x)
				print(alfabeto)
				q3(alfabeto,x)
			elif x == 'E':
				alfabeto.remove(x)
				print(alfabeto)
				q4(alfabeto)
			else:
				print("No aceptado... ",x)
				break

def q4(alfabeto):
	for x in alfabeto:
		if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9':
			#alfabeto.remove(x)
			print(alfabeto)
			q5(alfabeto,x)
		elif x == '-':
			alfabeto.remove(x)
			print(alfabeto)
			q6(alfabeto)
		elif x == '+':
			alfabeto.remove(x)
			print(alfabeto)
			q6(alfabeto)
		else:
			print("No aceptado... ",x)
			break


def q5(alfabeto,y):
	alfabeto.remove(y)
	if len(alfabeto) == 0:
		print("Estado de aceptacion q5...\n",alfabeto)
	else:
		for x in alfabeto:
			if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9':
				#alfabeto.remove(x)
				print(alfabeto)
				q5(alfabeto,x)
			else:
				print("No aceptado... ",x)
				break

def q6(alfabeto):
	for x in alfabeto:
		if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9':
			#alfabeto.remove(x)
			print(alfabeto)
			q5(alfabeto,x)
		else:
			print("No aceptado... ",x)
			break

""" Parte principal """
archivo = open("cadenas.txt","r")
for linea in archivo.readlines():
	print("**** Cadena = ",linea,"****")
	if linea[-1] == '\n':
		linea = linea[:-1]
	alfabeto = list(linea)
	for x in alfabeto:
		if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9':
			alfabeto.remove(x)
			print(alfabeto)
			q1(alfabeto)
		else:
			print("No aceptado... ",x)
			break
archivo.close()
