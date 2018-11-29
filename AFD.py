def q0(E):
	for i in E:
		if i == 'a':
			E.remove(i)
			print(E)
			q1(E)

def q1(E):
	for i in E:
		if i == 'b':
			E.remove(i)
			print(E)
			q3(E)

def q3(E):
	if len(E) == 0:
		print("\nEsta en el estado de aceptacion q3...")
	else:
		for i in range(len(E)):
			if 'c' in E:
				E.remove('c')
				print(E)
				if len(E) == 0:
					print("\nEsta en el estado de aceptacion q3...")
			else:
				print("\nNo es 'c'...")
				break


E = list("abccc")

q0(E)