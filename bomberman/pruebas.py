
final = []
a = open("src/levels/1/1.txt")

for linea in a.readlines():
    pos = 0
    for c in linea:
        if c == "\":
        final.append(linea[:pos])
        pos += 1