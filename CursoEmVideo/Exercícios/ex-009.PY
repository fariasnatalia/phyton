                                    # Pintando Parede
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados. 

largura = float(input('Largura da parede: ')) 
altura = float(input('Altura da parede: '))
area = largura * altura
print('Sua parede tem a dimensão de {} X {} e sua área é de {}m².'.format(largura, altura, area))       
tinta = area /2
print('Para pintar essa parede vc vai precisar de {} litros de tinta.'.format(tinta))                               