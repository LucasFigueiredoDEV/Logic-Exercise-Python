# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

total = 0
produtos_mais_de_mil = 0
produto_mais_barato = ''
valor_produto_mais_barato = 10000000000
while True:
    nome_produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o valor do produto: '))
    parada = input('Deseja continuar? S/N').upper()

    total += preco
    if preco > 1000:
        produtos_mais_de_mil += 1

    if preco < valor_produto_mais_barato:
        valor_produto_mais_barato = preco
        produto_mais_barato = nome_produto

    if parada == 'N' or parada == 'NÃO':
        break
    else:
        continue
print('-=' * 15)
print(f'TOTAL DA COMPRA: R${total:.2f}')
print()
print(f'{produtos_mais_de_mil} Produtos da sua compra custam mais de mil reais.')
print()
print(f'{produto_mais_barato} É o seu produto mais barato.')
print('-=' * 15)