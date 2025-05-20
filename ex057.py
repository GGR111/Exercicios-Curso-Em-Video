s = 'a'
while s not in 'MmFf':
    s = input('Qual o seu sexo [m/f]: ').lower().strip() [0]
if s == 'm':
    print('Sexo Masculino')
else:
    print('Sexo Feminino')
