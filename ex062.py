p = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
c = 1
while c != 0:
    print(p)
    p += r
    c -= 1
    if c == 0:
        c = int(input('Quantos mais: '))




