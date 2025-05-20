l1 = int(input('Digite o tamanho do primeiro lado do triangulo: '))
l2 = int(input('Digite o tamanho do segundo lado do triangulo: '))
l3 = int(input('Digite o tamanho do terceiro lado do triangulo: '))
if l1 > l2 >= l3:
    soma = l2+l3
    if l1 < soma:
        print('é um triangulo')
    else:
        print('Não é um triangulo')
if l1 > l3 >= l2:
    soma = l3+l2
    if l1 < soma:
        print('é um triangulo')
    else:
        print('Não é um triangulo')
if l2 > l1 >= l3:
    soma = l1+l3
    if l2 < soma:
        print('é um triangulo')
    else:
        print('Não é um triangulo')
if l2 > l3 >= l1:
    soma = l3+l1
    if l2 < soma:
        print('é um triangulo')
    else:
        print('Não é um triangulo')
if l3 > l1 >= l2:
    soma = l1+l2
    if l3 < soma:
        print('é um triangulo')
    else:
        print('Não é um triangulo')
if l3 > l2 >= l1:
    soma = l1+l2
    if l3 < soma:
        print('é um triangulo')
    else:
        print('Não é um triangulo')
if l1 == l2 == l3:
    print('é um triangulo')


