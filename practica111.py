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
			alfabeto.remove(x)
			print(alfabeto)
			q3(alfabeto)
		else:
			print("No aceptado... ",x)
			break

def q3(alfabeto):
	for x in alfabeto:
		if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9':
			alfabeto.remove(x)
			if len(alfabeto) == 0:
				print(alfabeto)
				print("Esta en el estado de aceptacion q3...")
				break
			q3(alfabeto)
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
			alfabeto.remove(x)
			print(alfabeto)
			q5(alfabeto)
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


def q5(alfabeto):
	for x in alfabeto:
		if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9':
			alfabeto.remove(x)
			print("Bandera")
			if len(alfabeto) == 0:
				print("Esta en el estado de aceptacion q5...")
			print("Bandera")
			q5(alfabeto)
		else:
			print("No aceptado... ",x)
			break

def q6(alfabeto):
	for x in alfabeto:
		if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9':
			alfabeto.remove(x)
			print(alfabeto)
			q5(alfabeto)
		else:
			print("No aceptado... ",x)
			break

#alfabeto = ['1','2','5','.','6','8','9']
alfabeto = ['1','2','5','.','6','8','9','E','+','1']

for x in alfabeto:
	if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9':
		alfabeto.remove(x)
		print(alfabeto)
		q1(alfabeto)
	else:
		print("No aceptado... ",x)
		break
