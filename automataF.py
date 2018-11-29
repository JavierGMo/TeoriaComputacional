def q1(a):
	for x in a:
		if x == 1:
			a.remove(x)
			q1(a)
			if len(a) == 0:
				print("Es estado de aceptacion......")
		elif x == 0:
			a.remove(x)
			q2(a)
		else:
			print("No se acepta")

def q2(a):
	for x in a:
		if x == 1:
			a.remove(x)
			q2(a)
			if len(a) == 0:
				print("No aceptado.......")
		elif x == 0:
			a.remove(x)
			q1(a)
		else:
			print("No se acepta")


a = [1,0,1,1,1,0]

q1(a)
"""



	 ->1<-
	 |   |			 ->
--->  |q1|  -- 0 --> q2  1
         <-- 0 --    <-

q1 estado de aceptacion......

"""
