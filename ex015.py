#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
#R$60 por dia e R$0,15 por Km rodado.

d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
vald = d * 60
valkm = km * 0.15
total = vald + valkm
print('valor pela quantidade de dias alugado R${}'.format(vald))
print('Valor pela quantidade de Km rodados R${:.2f}'.format(valkm))
print('Você deverá pagar no total R${:.2f}'.format(total))
