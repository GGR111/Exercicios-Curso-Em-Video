pm = float(input('Qual valor da mercadoria? '))
c = int(input('Opções:\n1- A vista em dinheiro = 10% de desconto'
              '\n2- A vista no cartão = 5% de desconto'
              '\n3- Em até 2x no cartão = preço normal'
              '\n4- Mais de 3x no cartão = 20% de juros'
              '\nOpção....'))
if c == 1:
    d = pm - (pm * (10 / 100))
    print('O valor da mercadoria era R${} com o desconto ficou R${}'.format(pm,d))
elif c == 2:
    d = pm - (pm * (5 / 100))
    print('O valor da mercadoria era R${} com o desconto ficou R${}'.format(pm, d))
elif c == 3:
    print('O valor da mercadoria continua os mesmos R${}'.format(pm))
elif c == 4:
    a = pm + (pm * (20 / 100))
    print('O valor da mercadoria era R${} com os juros ficou R${}'.format(pm, a))
else:
    print('Opção invalida')
