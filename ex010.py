#Crie um programa que leia quanto uma pessoa tem na carteira e  mostre quantos dólares ela pode comprar.
#Considerar valor do dólar a R$3.27

v = float(input('Quantos reais você tem? R$ '))
print('Você possui US${:.2f} dólares.'.format(v / 3.27))
