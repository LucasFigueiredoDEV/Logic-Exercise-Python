# Faça um programa que tenhha uma função chamada área(), que receba as dimensões
# de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(largura, altura):
    a = largura * altura
    print (f'A área de um terreno de {largura}x{altura} é de {a:.2f} m².')

b = float(input('Valor da largura: '))
h = float(input('Valor da altura: '))

area(b, h)