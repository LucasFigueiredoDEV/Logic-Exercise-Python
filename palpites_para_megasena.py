# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos e vai sortear quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
quant_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
lista_temp_jogos = []
jogos = []
tot = 1
while tot <= quant_jogos:
    cont = 0
    while True:
        sorteio_numero = randint(1, 60)
        if sorteio_numero not in lista_temp_jogos:
            lista_temp_jogos.append(sorteio_numero)
            lista_temp_jogos.sort()
            cont += 1
        if cont >= 6:
            break
    jogos.append(lista_temp_jogos[:])
    lista_temp_jogos.clear()
    tot += 1

print(f'-=' * 3, f'SORTEANDO {quant_jogos} JOGOS', f'-=' * 3)

for i, l in enumerate(jogos):

    print(f'JOGO {i + 1}: {l}')
        


