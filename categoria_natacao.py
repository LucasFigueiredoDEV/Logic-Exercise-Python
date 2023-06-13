# A confederação de Natação precisa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

print('\t Descubra a sua categoria na natação')
print()

ano = input('Digite o seu ano de nascimento: ')
ano_int = int(ano)
idade = 2023 - ano_int


if idade <= 9:
    print('CATEGORIA: MIRIM')
elif idade > 9 and idade <= 14:
    print('CATEGORIA: INFANTIL')
elif idade > 14 and idade <= 19:
    print('CATEGORIA: JUNIOR')
elif idade == 20:
    print('CATEGORIA: SÊNIOR')
else:
    print('CATEGORIA: MASTER')
