# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# O nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado tenha sido informado corretamente.


def ficha(nome = '<Desconhecido>', gols = 0):
    return print(f'O jogador {nome}, fez {gols}(s) no campeonato.')


nome_jogador = str(input('Nome do jogador: '))
numero_gols = str(input('Número de gols: '))

if numero_gols.isnumeric():
    numero_gols = int(numero_gols)
else:
    numero_gols = 0

if nome_jogador.strip() == '':
    ficha(gols= numero_gols)
else:
    ficha(nome_jogador, numero_gols)
