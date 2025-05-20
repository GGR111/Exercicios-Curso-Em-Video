from math import pow
a = float(input('Qual sua altura: '))
p = float(input('Qual seu peso: '))

imc = p/pow(a,2)
if imc < 18.5:
    print('Altura: {} metros\nPeso: {} quilos\nIMC: {:.2f}\nVoce esta abaixo do peso ideal'.format(a,p,imc))
elif imc < 25:
    print('Altura: {} metros\nPeso: {} quilos\nIMC: {:.2f}\nVoce esta no peso ideal'.format(a,p,imc))
elif imc < 30:
    print('Altura: {} metros\nPeso: {} quilos\nIMC: {:.2f}\nVoce esta com sobrepeso'.format(a,p,imc))
elif imc < 40:
    print('Altura: {} metros\nPeso: {} quilos\nIMC: {:.2f}\nVoce esta com obesidade'.format(a,p,imc))
elif imc >= 40:
    print('Altura: {} metros\nPeso: {} quilos\nIMC: {:.2f}\nVoce esta com obesidade morbida'.format(a,p,imc))