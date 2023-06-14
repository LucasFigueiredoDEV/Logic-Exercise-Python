# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.
masculino = 0
feminino = 0
soma_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
for pessoas in range(1, 5):
    nome = input(f'Digite o nome da {pessoas}ª pessoa: ')
    idade = int(input('Digite a sua idade: '))
    sexo = input('Digite [M] para sexo masculino e [F] para feminino: ').upper()
    soma_idade += idade

    if sexo == 'F' and idade < 20:
        feminino += 1
    elif sexo == 'M':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_mais_velho = nome


media_idade = soma_idade / 4



print(f'A média de idade das 4 pessoas é de {media_idade}')
print(f'O homem mais velho é {nome_homem_mais_velho} com {maior_idade_homem} de idade.')
print(f'{feminino} Mulheres têm menos de 20 anos.')