# Crie uma tupla preenchida com os 20 colocados da tabela do Campeonato de Futebol,
# na orem de colocação. Depois mostre: 
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.


tabela = ('Barcelona', 'Real Madrid', 'Atlético Madrid', 'Real Sociedad',
'Villarreal', 'Betis', 'Osasuna', 'Osasuna', 'Ath. Bilbao', 'Mallorca',
'Girona', 'Rayo Vallecano', 'Sevilla', 'Celta de Vigo', 'Cádiz', 'Getafe',
'Valencia', 'Almería', 'Real Valladolid', 'Espanyol', 'Elche')

while True:
    print( '''
    A) Apenas os 5 primeiros colocados.
    B) Os últimos 4 colocados da tabela.
    C) Uma lista com os times em ordem alfabética.
    D) Em que posição na tabela está o time do Real Madrid.
    ''')
    escolha = input('Digite a altenativa da sua escolha: ').upper()

    if escolha == 'A':
        print(f'Os 5 primeiros colocados da tabela: {tabela[0:5]}')
    elif escolha == 'B':
        print(f'Últimos 4 colocados da tabela: {tabela[-4::]}')
    elif escolha == 'C':
        print(f'TABELA EM ORDEM ALFABÉTICA: {sorted(tabela)}')
    elif escolha == 'D':
        print(f'O time do {tabela[1]} está em 2º colocado.')
    elif escolha == 'SAIR':
        break
    else:
        print('Escolha uma das opções ou digite "Sair", para sair!')

print('FIM!')
