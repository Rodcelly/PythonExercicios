#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

s = float(input('Informe o seu salário atual: '))
ns = ((s * 15) / 100) + s
print('Seu novo salário é: {:.2f}'.format(ns))
