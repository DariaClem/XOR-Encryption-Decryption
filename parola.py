f = open("input.txt", "r")
g = open("output", "rb")

textnormal = f.read()
textbinar = g.read()
text = ""

for i in range(10, 17):
    text = ""
    for j in range(0, 2*i):
        text += chr(ord(textnormal[j]) ^ textbinar[j])
    if text[:i]*2 == text:
        print(text[:i])
        break

