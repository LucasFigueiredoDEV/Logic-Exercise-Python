# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa que vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler o quantidade de gols feitos em cada partida.
# No final tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
total_gols = 0
lista_gols = []
jogador['Nome'] = input('Nome do jogador: ')
partidas_jogadas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for partidas in range(0, partidas_jogadas):
    gols_por_partida = int(input(f'Quantos gols na partida {partidas + 1}?'))
    total_gols += gols_por_partida
    lista_gols.append(gols_por_partida)

jogador['Gols'] = lista_gols
jogador['Total'] = total_gols


print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)

print(f'O jogador {jogador["Nome"]} jogou {partidas_jogadas}.')
for i,v in enumerate(lista_gols):
    print(f'=> Na partida {i + 1}, fez {v} gols.')

print(f'Foi um total de {total_gols} gols.')