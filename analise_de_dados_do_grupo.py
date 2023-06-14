# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
masculino = 0
feminino_menos_vinte = 0
mais_dezoito = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo [M]asculino ou [F]eminino: ').upper()
    if idade > 18:
        mais_dezoito += 1

    if sexo == 'M' or sexo == 'MASCULINO':
        masculino += 1
    elif sexo == 'F' or sexo == 'FEMININO':
        if idade < 20:
            feminino_menos_vinte += 1

    parada = input('Você deseja continuar? S/N  ').upper()
    if parada == 'N':
        break
    else:
        continue
print(f'{mais_dezoito} Pessoas tem mais de 18 anos.')
print(f'{masculino} Homens foram cadastrados.')
print(f'{feminino_menos_vinte} Mulheres tem menos de 20 anos.')

