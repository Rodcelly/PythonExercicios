#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = float(input('Qual número você deseja analisar? '))
d = n * 2
t = n * 3
r = n ** 2
print('O dobro é {}, o triplo é {} e a raiz é {}'.format(d, t, r))
print('De forma respectiva, em ordem, número, dobro, triplo e raiz: ', end='')
print(n, d, t, r)
