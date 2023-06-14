# Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador perder mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.
from random import randint
vitorias = 0
while True:
    jogada = input('Você escolhe [P]ar ou [I]mpar? ').upper()
    if jogada == 'P' or jogada == 'PAR' or jogada == 'I' or jogada == 'IMPAR':
        computador = randint(0, 10)
        valor_jogador = int(input('Digite um valor: '))
        resultado = (valor_jogador + computador) % 2
        if jogada == 'P' or jogada == 'PAR':
            if resultado == 0:
                print('Você venceu!')
                vitorias += 1
                continue
            else:
                print('Você perdeu!')
                break
        else:
            if resultado != 0:
                print('Você venceu!')
                vitorias += 1
                continue
            else:
                print('Você perdeu!')
                break
    elif jogada == 'SAIR':
        break
    else:
        print('Escolha uma das opções ou digite "sair" para sair do jogo.')
        continue
print('-=' * 15)
print()
print(f'TOTAL DE VITÓRIAS: {vitorias}')
print()
print('-=' * 15)
print('FIM!')