# Crie um programa que faça o computador jogar jokenpô com você

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')

print('-=' * 11)
print(f'O computador escolheu {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)



if computador == jogador:
    print('Empate')
elif computador == 0 and jogador == 2:
    print('Computador venceu!')
elif computador == 0 and jogador == 1:
    print('Jogador venceu!')
elif computador == 1 and jogador == 0:
    print('Computador venceu!')
elif computador == 1 and jogador == 2:
    print('Jogador venceu!')
elif computador == 2 and jogador == 0:
    print('Jogador venceu!')
elif computador == 2 and jogador == 1:
    print('Computador venceu!')
else:
    print('Jogada inválida!')