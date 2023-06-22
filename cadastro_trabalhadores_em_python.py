# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-os(com idade) em um dicionário, se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além
# da idade, com quantos anos a pessoa vai se aposentar.

cadastro = {}

cadastro['Nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
cadastro['ctps'] = int(input('Carteira de trabalho: '))

cadastro['Idade'] = 2023 - ano_nascimento

if cadastro['ctps'] != 0:
    cadastro['Ano de contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Valor do salário: '))
    cadastro['Aposentadoria'] = cadastro['Ano de contratação'] + 35

print(cadastro)
print()

for k, v in cadastro.items():
    print(f'O {k} tem o valor {v}.')
