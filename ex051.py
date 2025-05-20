p = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
for a in range (p, (r*10)+p, r):
    print(a)