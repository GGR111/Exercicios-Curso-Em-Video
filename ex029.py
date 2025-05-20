vc = int(input('Velocidade do carro: '))

if vc <= 80:
    print('Sua velocidade era {}km/h !! Dentro do limite de velocidade'.format(vc))
else:
    multa = (vc-80)*7
    print('Sua velocidade era {}km/h !!!, precisa pagar uma multa de R${} !!'.format(vc,multa))