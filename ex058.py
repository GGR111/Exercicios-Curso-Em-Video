import random
from time import sleep
m = random.randint(1, 10)
j = 0
t = 0
while j != m:
    j = int(input('\033[31mMAQUINA: EU TE DESAFIO, ESCOLHA UM NUMERO:\033[m '))
    print('MAQUINA: DEIXA EU VER...')
    sleep(1)
    r = random.randint(1, 3)
    if j != m and j < m:
        if r == 1:
            print('MAQUINA: AHAHAHAHHA EU VENCI, VOCE JOGOU MT BAIXO, TENTA DENOVO')
        elif r == 2:
            print('MAQUINA: EU NUNCA PERDERIA PRA VOCE, VOCE JOGOU MT BAIXO, TENTA DENOVO')
        elif r == 3:
            print('MAQUINA: É SÓ ISSO QUE VOCE TEM???? VOCE JOGOU MT BAIXO, TENTA DENOVO')
    elif j != m and j > m:
        if r == 1:
            print('MAQUINA: AHAHAHAHHA EU VENCI, VOCE JOGOU MT ALTO, TENTA DENOVO')
        elif r == 2:
            print('MAQUINA: EU NUNCA PERDERIA PRA VOCE, VOCE JOGOU MT ALTO, TENTA DENOVO')
        elif r == 3:
            print('MAQUINA: É SÓ ISSO QUE VOCE TEM???? VOCE JOGOU MT ALTO, TENTA DENOVO')
    t += 1
if t == 1:
    print('MAQUINA: IMPOSSIVEL, VOCE CONSEGUIU DE PRIMEIRA??????')
else:
    print('MAQUINA: HA EU PERDI MAS VOCE TENTOU {} VEZES'.format(t))

