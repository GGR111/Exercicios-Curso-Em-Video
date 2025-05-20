n = 0
c = 0
s = 0
while n != 999:
    n = int(input('Digite um numero, para parar digite (999): '))
    c+=1
    s+=n
print('Foram digitados {} numeros e a soma foi {}'.format(c-1,s-999))