# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 15:08:26 2018

@author: Javier Gonzalez M
"""
j = 0
cont = 0
lm,primo = [2,3,4,5,7,8,9], []

for x in range(2,100):
	for y in lm:
		if x%y == 0:
			cont += 1
			print(str(cont) + " x: " +str(x))
			if cont >= 2:
				#print(str(x) + " no es primo")
				pass
			else:
				primo.append(x)
	cont = 0

print(primo)