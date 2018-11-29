import re


patron = re.compile(r'\b[a-z]*a[a-z]*e[a-z]*i[a-z]*o[a-z]*u[a-z]*\b')



f = open ('codi.txt','r')
mensaje = f.read()
f.close()


m = patron.search(mensaje)


print(m.group())


