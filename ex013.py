#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desonto.

p = float(input('Qual é o valor do produto? '))
vf = p - ((p * 5) / 100)
print('O valor do produto com 5% de desconto é: R${:.2f}'.format(vf))
