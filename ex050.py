s = 0
for a in range (0, 6):
    n = int(input('Digite um numero: '))
    if n%2 == 0:
        s += n
print('A soma dos numeros pares é {}'.format(s))