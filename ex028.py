import random
from time import sleep
t = int(input('Digite um numero entre 1 e 5: '))
a = random.randint(1,5)
print('PROCESSANDO')
sleep(2)
if t == a:
    print('O numero escolhido foi {} e o sorteado foi {}, '
          'Em cheio parabens!!!'.format(a,t))
else:
    print('O numero escolhido foi {} e o sorteado foi {}, '
          'Boa sorte na proxima'.format(a,t))