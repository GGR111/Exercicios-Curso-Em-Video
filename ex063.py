c = int(input('Digite um numero: '))
n1 = 0
n2 = 1
# 0 1 1 2 3 5 8 13 21 34 55
while c != 0:
    print(n1)
    temp = n1
    n1 = n1 + n2
    n2 = temp
    c -= 1
