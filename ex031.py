d = int(input('Digite a ditancia em km da viagem: '))
if d <=200:
    v = d*0.50
    print('Viajando {}km sera cobrado R${}'.format(d,v))
else:
    v = d*0.45
    print('viajando {}km sera cobrado R${}'.format(d,v))