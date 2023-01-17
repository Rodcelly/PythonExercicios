#Faça um programa que leia um número inteiro e mostre o seu secessor e seu antecessor.

n = int(input('Digite um número: '))
s = n - 1
a = n + 1
print("O seu antecessor é {}, o seu sucessor é {}, o seu número é {}.".format(s, a, n), end=' Em ordem, antecessor, número e sucessor: ')
print(s, n, a)
