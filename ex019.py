from random import choice
a1 = input('nome do primeiro aluno: ')
a2 = input('nome do segundo aluno: ')
a3 = input('nome do terceiro aluno: ')
a4 = input('nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
s = choice(lista)

print('O aluno escolhido foi o {}!!!!!!!!!!!!!!'.format(s))
