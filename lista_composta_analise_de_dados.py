# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = 0
lista = []
dados = []
maior = 0
menor = 0
while True:
    lista.append(str(input('Digite o nome: ')))
    lista.append(float(input('Digite o peso: ')))
    pessoas += 1
    if len(dados) == 0:
        maior = lista[1]
        menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    
    dados.append(lista[:])
    lista.clear()
    saida = input('Deseja sair: S/N  ').upper()
    if saida == 'S' or saida == 'SIM' or saida == 'SAIR':
        break
    else: 
        continue




print('-='*30)
print(f'Foram cadastradas {pessoas} pessoas.')
print(f'O maior peso foi de {maior}Kg. e foi de: ', end='')
for p in dados:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}Kg. e foi de: ', end='')
for p in dados:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()
print('-='*30)