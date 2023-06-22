# Faça um programa que leia nome e média de um aluno, guardando também em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
dicionario = {}

dicionario['Aluno'] = str(input('Nome: '))
dicionario['Média'] = float(input(f'Média de {dicionario["Aluno"]}: '))


for chave, valor in dicionario.items():
    print(f'Nome é igual a {dicionario["Aluno"]}.')
    print(f'Média é igual a {dicionario["Média"]}.')
    if dicionario['Média'] >= 7.0:
        print('Situação é igual a APROVADO.')
    else:
        print('Situação é igual a REPROVADO!')