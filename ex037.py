n = int(input('Digite um numero: '))
op = int(input('Opções: \n1 - converte para binario'
               '\n2 - converte para octal'
               '\n3 - converte para hexadecimal'
               '\nOpção.....'))

if op == 1:
    print('A conversão do numero {} em binario é igual a :'.format(n))
    print(bin(n)[2:])
elif op == 2:
    print('A conversão do numero {} em octal é igual a :'.format(n))
    print(oct(n)[2:])
elif op == 3:
    print('A conversão do numero {} em hexadecimal é igual a :'.format(n))
    print(hex(n)[2:].upper())
else:
    print('Opção invalida seu burro')