n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
print('[ 1 ] - Soma\n'
      '[ 2 ] - Multiplica\n'
      '[ 3 ] - Maior\n'
      '[ 4 ] - Adiciona outro numero\n'
      '[ 5 ] - Encerra o programa')
m = int(input('Digite um numero do menu: '))
while m != 5:
    if m == 1:
        print('A soma de {} + {} = {}'.format(n1, n2, n1+n2))
    elif m == 2:
        print('A multiplicação de {} * {} = {}'.format(n1, n2, n1 * n2))
    elif m == 3:
        if n1>n2:
            print('{} é maior que {}'.format(n1,n2))
        elif n2>n1:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('{} é igual a {}'.format(n1, n2))
    elif m == 4:
        t = int(input('Qual numero deseja trocar (1 ou 2) ou se quiser trocar os 2 (0)? '))
        if t == 1:
            n1 = int(input('Novo numero: '))
        elif t == 2:
            n2 = int(input('Novo numero: '))
        elif t == 0:
            n1 = int(input('Novo numero 1: '))
            n2 = int(input('Novo numero 2: '))
        else:
            print('\33[31mComando invalido\33[m')

    elif m > 5 or m < 1:
        print('\33[31mComando invalido\33[m')
    m = int(input('Digite outro numero do menu: '))