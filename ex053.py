p = input('Digite uma palavra: ').strip().lower()
p = p.replace(' ','')
i = p[::-1]

if p == i:
    print('{} ao contrario fica {} ou seja é Palindromo'.format(p,i))
else:
    print('{} ao contrario fica {} ou seja não é Palindromo'.format(p,i))

