#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Qual valor em metros você deseja verificar? '))
c = m * 100
mm = m * 1000
print('{} metros equivalem a {:.0f} centímetros e a {:.0f} milímetros.'.format(m, c, mm))
