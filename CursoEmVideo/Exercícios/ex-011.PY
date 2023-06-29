                                    # Reajuste Salarial
#  Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.       
salario = float(input('Digite o valor referente ao salário: '))    
desconto = salario * 15 /100
novo_salario = salario - desconto


print('O salário com o desconto ficou no valor de: {}'.format(novo_salario))                   
 
 
 # ESSA FORMA ANTERIOR É UMA FORMA DE RESOLVER COM UM DESCONTO ESPECÍFICO, VAMOS FAZER COM UMA FORMA DINÂMICA RECEBENDO A PORCENTAGEM PELO TECLADO!
 
SALARIO = float(input('Digite o valor referente ao salário:'))
DESCONTO = int(input('Quanto você como funcionário, gostaria de receber como desconto? '))
NOVO_SALARIO = SALARIO - (SALARIO * DESCONTO / 100)

print('O desconto foi de {}, \n Então o resultado do valor referente ao salário é de: {}'.format(DESCONTO, NOVO_SALARIO))
 