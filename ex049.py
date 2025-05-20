n = int(input('Digite um numero: '))
print('='*27)
print('A tabuado do numero {} é: '.format(n))
for a in range (1,11):
    m = a * n
    print('{} x {} = {}'.format(n,a,m))
    m = 1
print('='*27)
