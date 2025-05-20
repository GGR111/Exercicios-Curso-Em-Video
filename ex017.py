from math import hypot
c1 = int(input('Digite o primeiro cateto: '))
c2 = int(input('Digite o segundo cateto: '))
h = hypot(c1,c2)
print('O resultado da hipotenusa com os catetos {} e {} é {}!!!'.format(c1,c2,h))