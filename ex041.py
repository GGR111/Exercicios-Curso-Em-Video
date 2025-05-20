a = 2025
c = int(input('Qual ano de nascimento do competidor: '))
id = 2025 - c

if id < 9:
    print('CATEGORIA MIRIM')
elif id < 14:
    print('CATEGORIA INFANTIL')
elif id < 19:
    print('CATEGORIA JUNIOR')
elif id < 20:
    print('CATEGORIA SENIOR')
elif id >= 20:
    print('CATEGORIA MASTER')
