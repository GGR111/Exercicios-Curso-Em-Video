f = input('Digite uma frase: ').strip().lower()
qa = f.count('a')
pa = f.find('a')
ua = f.rfind('a')
print('''
quantos a's tem : {}
primeiro a : {}
ultimo a : {}
'''.format(qa,pa+1,ua+1))