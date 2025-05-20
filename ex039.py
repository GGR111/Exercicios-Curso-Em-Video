import time
a = time.localtime().tm_year
i = int(input('Qual o ano do seu nascimento: '))
id = a-i

if id > 18:
    at = id - 18
    print('Com {} anos, voce esta a {} atradado para se alistar!!'.format(id,at))
elif id < 18 and i <= a:
    ft = 18 - id
    print('Com {} anos, falta {} ano(s) para se alistar!!'.format(id,ft))
elif id == 18:
    print('com {} anos, voce já pode se alistar!!'.format(id))
elif i > a:
    print('Data de nascimento invalida!!!!')