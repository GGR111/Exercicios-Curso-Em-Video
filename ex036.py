vc = float(input('Qual valor da Casa? '))
sal = float(input('Quanto voce ganha por mes? '))
p = int(input('em quantas parcelas deseja pagar? '))

vp = vc/p
m = sal*(30/100)

if vp <= m:
    print('Com o salario de R${}, o senhor tem R${} de margem'.format(sal,m))
    print('Em {} parcelas o valor de cada parcela sai a R${} por mes'.format(p,vp))
    print('Parabens, voce pode pegar um emprestimo para comprara casa!!!')
else:
    print('Com o salario de R${}, o senhor tem R${} de margem'.format(sal, m))
    print('Em {} parcelas o valor de cada parcela sai a R${} por mes'.format(p, vp))
    print('Infelizmente o senhor não possui margem suficiente para comprar a casa')
