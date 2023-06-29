#Dissecando uma Variável {Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.}
a = input('Digite algo:')

print('O tipo primitivo desse valor é',type(a))
print('-----------------------')

print('Só tem espaços?', a.isspace()) #verificando se só tem espaços {FALSE OU TRUE}
print('-----------------------')

print('É um número?', a.isnumeric()) #verificando se é um número
print('-----------------------')

print('É alfabético?', a.isalpha()) #verificando se é alfabético
print('-----------------------')

print('É alfanumérico?', a.isalnum())#verificando se tem letras e números
print('-----------------------')

print('Está em maiúsculas?', a.isupper())#verificando se as letras sÃo MAIÚSCULAS
print('-----------------------')

print('Está em maiúsculas?', a.islower())#verificando se as letras são MENÚSCULAS