#Faça um prorama que leia a largura e a altura de uma parede em metros.
#Calcule a sua área e a quantidade de tinta necessaria para pinta-la.
#Sabendo que cada litro de tinta pinta uma área de 2m².

l = float(input('Qual a largura da parede em metros? '))
a = float(input('Qual a altura da parede em metros? '))
ca = l * a
qtn = ca / 2
print('A área da parede é de {:.2f}m² e será necessário {:.2f} litros de tinta para pinta-la.'.format(ca, qtn))
