s = 0
sm= 0
ih= 0
for a in range (1, 5):
    n = input('Qual seu nome? ')
    i = int(input('Qual sua idade? '))
    se = input('Qual seu sexo? ').lower().strip()
    s +=i
    if se == 'm' or se == 'mulher' or se == 'feminino' or se == 'f':
        if i <=20:
            sm+=1
    if se == 'h' or se == 'homem' or se == 'masculino':
        if ih < i:
            ih = i
media = s/4
print('A media da idade é de {:.2f} de idade\n'
      'O homem mais velho tem {} anos\n'
      'tem {} mulheres com menos de 20 anos\n'.format(media,ih,sm))

