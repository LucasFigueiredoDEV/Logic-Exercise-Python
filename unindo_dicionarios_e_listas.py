# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
# os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.

lista = []
dicionario = {}
lista_mulheres = []
pessoas = 0
soma_idade = 0

while True:
    dicionario.clear()
    dicionario['Nome'] = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo: [M/F] ')).upper()
        if sexo == 'M' or sexo == 'F':
            dicionario['Sexo'] = sexo
            if sexo == 'F':
                lista_mulheres.append(dicionario['Nome'])
            break
        else:
            print('Digite uma das opções.')
            continue
    dicionario['Idade'] = int(input('Idade: '))
    soma_idade += dicionario['Idade']
    lista.append(dicionario.copy())
    pessoas += 1
    saida = str(input('Deseja continuar? [S/N]')).upper()
    if saida in 'Nn':
        break



media = soma_idade / pessoas

print('-=' * 30)

print(f'- O grupo tem {pessoas} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for mulheres in lista_mulheres:
    print(f'{mulheres}'.split(), end=' ')

print()
print('- Lista de pessoas que estão acima da média:')
for p in lista:
    if p['Idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('-=' * 30)
print()

print('<< ENCERRADO >>')




