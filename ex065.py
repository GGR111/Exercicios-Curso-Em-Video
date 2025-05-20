c = 'sim'
s = 0
cont = 0
ma = 0
me = 99999999999999999999999999999
while c == 'sim':
    n = int(input('Digite um numero: '))
    s += n
    if n > ma:
        ma = n
    if n < me:
        me = n
    c = input('Deseja continuar? (sim/nao): ').lower().strip()
    if c != 'nao' and c != 'sim':
        print('Codigo invalido, o programa continuará! ')
        c = 'sim'
    cont +=1
print('\33[31m=-\33[m'*20)
print('Media = {}\n'
      'Maior valor = {}\n'
      'Menor valor = {}'.format(s/cont,ma,me))
print('\33[31m=-\33[m'*20)