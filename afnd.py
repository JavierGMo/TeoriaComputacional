#Expresion regular: ab*|a*ba
def q0():
	pass

def q1(E):
	for i in E:
		if i == 'b':
			print(E)
			E.remove(i)
			if len(E) == 0:
				print("\nEsta en el estado de aceptacion q1...")
				break
			else:
				pass


def q2():
	pass

# ******************* main del programa ****************************** #

E = list("abbbb")

print(E)

if E[0] == 'a':
	del E[0]
	print(E)
	q1(E)


