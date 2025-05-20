n = input('digite um numero de 0 a 9999: ').zfill(4)
print('''
milhar:  {}
centena: {}
dezena:  {}
unidade: {}
'''.format(n[0],n[1],n[2],n[3]))