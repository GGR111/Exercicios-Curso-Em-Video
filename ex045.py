from random import randint
from time import sleep
op = int(input('Opçoes:\n1- Pedra'
               '\n2- Papel'
               '\n3- Tesoura'
               '\nOpções....'))
if op == 1:
    op = 'PEDRA'
elif op == 2:
    op = 'PAPEL'
elif op == 3:
    op = 'TESOURA'

m = randint(1,3)
if m == 1:
    m = 'PEDRA'
elif m == 2:
    m = 'PAPEL'
elif m == 3:
    m = 'TESOURA'
sleep(0.85)
print('MAQUINA: Pedra')
sleep(0.85)
print('MAQUINA: Papel')
sleep(0.85)
print('MAQUINA: Ou tesouuuura')
sleep(1.2)
if (m == 'PEDRA' and op == 'TESOURA') or (m == 'PAPEL' and op == 'PEDRA') or (m == 'TESOURA' and op == 'PAPEL'):
    print('MAQUINA:VOCE ESCOLHER {} E EU ESCOLHI {}, EU GANHEI SEU PERDEDOR HAHAHAHAHAHAHHA'.format(op,m))
elif (op == 'PEDRA' and m == 'TESOURA') or (op == 'PAPEL' and m == 'PEDRA') or (op == 'TESOURA' and m == 'PAPEL'):
    print('MAQUINA:VOCE ESCOLHER {} E EU ESCOLHI {} EU EU.... eu perdi???'.format(op,m))
else:
    print('MAQUINA:VOCE ESCOLHER {} E EU ESCOLHI {} HAHAHAHA EU GA... AH FOI EMPATE'.format(op,m))
