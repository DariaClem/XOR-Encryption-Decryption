import sys

fisierinput = sys.argv[1]
parola = sys.argv[2]
fisieroutput = sys.argv[3]

f = open(fisierinput, "rb")
g = open(fisieroutput, "w")

text = f.read()

nr = 0
n = len(parola)

for ch in text:
    a = ch
    b = ord(parola[nr])
    g.write(chr(a ^ b))
    nr += 1
    if nr == n:
        nr = 0

g.close()
f.close()