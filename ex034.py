sal = float(input('Digite seu salario: '))
if sal >=1250:
    aum = sal+(sal*10/100)
    print('Seu salario era R${} e passou a ser R${}!!!'.format(sal,aum))
else:
    aum = sal+(sal*15/100)
    print('Seu salario era R${} e passou a ser R${}!!!'.format(sal,aum))