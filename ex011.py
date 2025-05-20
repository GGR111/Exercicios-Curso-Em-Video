l1 = float(input('lado 1 da parede: '))
l2 = float(input('lado 2 da parede: '))
a = l1*l2
b = a/2
print('para pintar uma parede de {:.2f}m² é preciso de {:.2f} baldes de tinta'.format(a,b))