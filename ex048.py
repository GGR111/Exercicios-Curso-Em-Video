s = 0
cont = 0
for a in range(0, 501):
    if (a % 2 == 1) and (a % 3 == 0):
        s += a
        cont += 1
print('A soma é {} e foram somados {} numeros'.format(s,cont))


