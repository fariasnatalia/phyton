                                    # Calculando Descontos
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.


preco = float(input('Qual  preço do produto?'))
desconto = preco * 5 / 100
preco_novo = preco - desconto
print('O produto que custava R${} com o desconto de 5% vai custar R${:.0f}'.format(preco, preco_novo))



#  PARA CALCULAR A PORCENTAGEM BASTA MULTIPLICAR O VALOR DO PREÇO PELO DESCONTO DESEJADIO E DIVIDIR POR 100 EX: 5 % DE DESCONTO :  PREÇO * 5 / 100   OU   10 %    PREÇO * 10 / 100  

# ESSA FORMA ANTERIOR É UMA FORMA DE RESOLVER COM UM DESCONTO ESPECÍFICO de 5%, VAMOS FAZER COM UMA FORMA DINÂMICA RECEBENDO A PORCENTAGEM PELO TECLADO!                 

preco = float(input('Qual o preço do produto? R$'))
desconto = int(input('Quanto você irá oferecer de desconto para o cliente? '))
preco_novo = preco - (preco * desconto / 100)        
print('O produto que custava R${} com o desconto de {}% vai custar R${:.0f}'.format(preco, desconto, preco_novo))  


                