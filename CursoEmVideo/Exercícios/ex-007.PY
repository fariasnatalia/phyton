                                    # Tabuada
# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.   

# ESSA FORMA É A MAIS CANSATIVA/ ESSA TABUADA EXIBE VALORES DE NÚMEROS INTEIROS

num = int(input('Digite um número para ver a sua tabuada sem casas decimais: '))                   
print('[{}] X [{}] = [{}]'.format(num, 1, num *1))
print('[{}] X [{}] = [{}]'.format(num, 2, num *2))
print('[{}] X [{}] = [{}]'.format(num, 3, num *3))      
print('[{}] X [{}] = [{}]'.format(num, 4, num *4))
print('[{}] X [{}] = [{}]'.format(num, 5, num *5))
print('[{}] X [{}] = [{}]'.format(num, 6, num *6))
print('[{}] X [{}] = [{}]'.format(num, 7, num *7))
print('[{}] X [{}] = [{}]'.format(num, 8, num *8))
print('[{}] X [{}] = [{}]'.format(num, 9, num *9))
print('[{}] X [{}] = [{}]'.format(num, 10, num *10))
   
print('----------------------------------')  
   # FORMA MAIS  ENXUTA DE CALCULAR A TABUADA/ ESSA TABUADA EXIBE VALORES COM PONTO FLUTUANTE

NUM = float(input('Digite um número para ver a sua tabuada com  casas decimais'))                                             
for fator in range(1,11):
    print(f'[{NUM}] X [{fator}] = {NUM * fator}')
                                                         