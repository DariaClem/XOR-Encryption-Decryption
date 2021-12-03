import sys

parola = sys.argv[1]
fisierinput = sys.argv[2]
fisieroutput = sys.argv[3]

f = open(fisierinput, "r")
g = open(fisieroutput, "wb")
text = f.read()

nr = 0
n = len(parola)

for ch in text:
    a = ord(ch)
    b = ord(parola[nr])
    g.write(bytes(chr(a ^ b), 'utf-8'))
    nr += 1
    if nr == n:
        nr = 0

f.close()
g.close()
