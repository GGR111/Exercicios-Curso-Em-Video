km = float(input('Andou quantos km com o carro? '))
d = int(input('Ficou quantos dias com o carro? '))
vkm = km * 0.15
vd = d * 60
tot = vkm + vd

print('Voce alugou o carro por {} dias que deu R${:.2f} e andou {}km que deu R${:.2f} totalizando R${:.2f}'.format(d,vd,km,vkm,tot))