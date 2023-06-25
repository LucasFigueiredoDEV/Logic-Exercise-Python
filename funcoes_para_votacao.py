# Crie um programa que tenha uma função chamada voto() que vai
# receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO
# OPCIONAL OU OBRIGATÓRIO nas eleições.


def voto(nascimento):
    idade = 2023 - nascimento

    if idade >= 18 and idade <= 70:
        return print(f'Com {idade} anos: seu voto é OBRIGATÓRIO')
    elif idade == 16 or idade == 17 or idade > 70:
        return print(f'Com {idade} anos: seu voto é OPCIONAL')
    else:
        return print(f'Com {idade} anos: seu voto é NEGADO')
    

ano_nascimento = int(input('Ano de nascimento: '))

voto(ano_nascimento)