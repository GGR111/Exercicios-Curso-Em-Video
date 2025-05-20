pg = 0
pm = 999999999999
for a in range (1, 6):
    c = int(input('Qual o seu peso? '))
    if pg < c:
        pg=c
    if pm>c:
        pm=c
print('O maior peso foi {} e o menor foi {}'.format(pg,pm))
