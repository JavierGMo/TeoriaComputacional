import re

""" Formato para numeros complejos: a + bi a>0 & b>0"""

#patron = re.compile(r'([0-9(\.)?]+[+][0-9(\.)?]+i|[-][0-9.(\.)?]+[-][0-9(\.)?]+i|[-][0-9(\.)?]+[+][0-9(\.)?]+i|[0-9(\.)?]+[-][0-9(\.)?]+i)')
patron = re.compile(r'[-]?[0-9.]*[+]?[-]?[0-9.]*i')



f = open ('complejos.txt','r')
mensaje = f.read()
f.close()

m = patron.findall(mensaje)




print(m)
