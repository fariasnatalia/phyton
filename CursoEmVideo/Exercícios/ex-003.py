#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um número:'))
a = n - 1
s = n + 1
print('Analisando o valor [{}], seu antecessor é : [{}] e o sucessor é : [{}]'.format(n, a, s))

print(' AGORA VAMOS MOSTRAR OTRA FORMA DE ENCONTRAR O ANTECESSOR E O SUCESSOR')

n = int(input('Digite um número:'))
print('Segundo o valor [{}], seu antecessor é : [{}] e o sucessor é : [{}]'.format(n, (n-1), (n+1)))