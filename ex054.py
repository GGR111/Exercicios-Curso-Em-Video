import datetime
at = datetime.date.today().year
sa = 0
sc = 0
for a in range (1, 8):
     ano = int(input('Que ano voce nasceu: '))
     id = at - ano
     if id >= 21:
         sa+=1
     else:
         sc+=1
print('das 7 pessoas, {} são adultos e {} são criaças'.format(sa,sc))

