l1 = int(input('Primeiro lado: '))
l2 = int(input('Segundo lado: '))
l3 = int(input('Terceiro lado: '))

if (l1 < (l2+l3) and l2 < (l1+l3) and l3 < (l1+l2)):
    if l1==l2==l3:
        print('é um triangulo')
        print('triangulo equilatero!!!')
    elif l1==l2!=l3 or l3==l2!=l1 or l3==l1!=l2:
        print('é um triangulo')
        print('triangulo isosceles!!!')
    elif l1!=l2!=l3:
        print('é um triangulo')
        print('triangulo escaleno!!!')
else:
    print('Não é um triangulo')
