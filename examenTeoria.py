import re

patron = re.compile(r'[\w.%+-]+@[a-zA-Z]+\.[a-zA-Z]{3,5}[\w.%+-]+\n[\w.%+-]*')


forma = """From: someone@example.com
To: someone_else@example.com
Subject: An RFC 822 formatted message

This is the plain text body of the message. Note the blank line
between the header information and the body of the message."""


print(patron.search(forma))
#print(p1.search(forma))
#print(p2.search(forma))

#m.group()




