n = input('Nome completo: ')
d = n.split()
pn = d[0]
un = d[-1]
print('''
primeiro nome = {}
Ultimo nome =  {}
'''.format(pn,un))