from math import sin,cos,tan,radians
n = float(input('Digite um angulo: '))
s = sin(radians(n))
c = cos(radians(n))
t = tan(radians(n))
print('Dado o angulo {}º temos o seno= {:.2f}, o cosseno{:.2f}, e a tangente{:.2f}'.format(n,s,c,t))