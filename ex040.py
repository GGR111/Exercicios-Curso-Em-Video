n1 = float(input('Qual sua primeira nota? '))
n2 = float(input('Qual a segunda nota? '))
m = (n1+n2)/2

if m < 5.0:
    print('Tirando a nota {} e a nota {}, temos a media {}\nREPROVADO!!!!'.format(n1,n2,m))
elif m >=5 and m <=6.9:
    print('Tirando a nota {} e a nota {}, temos a media {}\nRECUPERAÇÃO!!!!'.format(n1,n2,m))
elif m >= 7.0:
    print('Tirando a nota {} e a nota {}, temos a media {}\nPARABENS, APROVADO!!!!'.format(n1,n2,m))
