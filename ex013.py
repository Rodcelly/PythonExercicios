#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

s = float(input('Informe o seu salário atual R$ '))
ns = ((s * 15) / 100) + s
print('Seu novo salário é R$ {:.2f}'.format(ns))
