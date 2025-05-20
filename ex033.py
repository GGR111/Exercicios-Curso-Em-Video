n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
if n1 > n2 > n3:
    print('O {} é o maior numero e o {} é o menor'.format(n1,n3))
if n1 > n3 > n2:
    print('O {} é o maior numero e o {} é o menor'.format(n1,n2))
if n2 > n1 > n3:
    print('O {} é o maior numero e o {} é o menor'.format(n2,n3))
if n2 > n3 > n1:
    print('O {} é o maior numero e o {} é o menor'.format(n2,n1))
if n3 > n1 > n2:
    print('O {} é o maior numero e o {} é o menor'.format(n3,n2))
if n3 > n2 > n1:
    print('O {} é o maior numero e o {} é o menor'.format(n3,n1))
