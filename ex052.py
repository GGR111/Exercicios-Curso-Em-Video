d = 1
n = int(input('Digite um numero: '))
for a in range (n, 1, -1):
    if n % a == 0:
        d += 1
if d == 2:
    print('é um numero primo')
else:
    print('Não é um numero primo')
