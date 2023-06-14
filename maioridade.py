# Crie um programa que leia o ano de nascimento de sete pessoas, No final, 
# mostre quantas pessoas ainda não atingiram a maioridade já são maiories.
ano_atual = 2023
pessoas_maior_dezoito = 0
pessoas_menor_dezoito = 0
for c in range(0, 7):
    ano_nascimento = int(input('Digite o seu ano de nascimento: '))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        pessoas_maior_dezoito += 1
    else:
        pessoas_menor_dezoito += 1
print(f'{pessoas_maior_dezoito} pessoas atingiram a maioridade.')
print(f'{pessoas_menor_dezoito} pessoas NÃO atingiram a maioridade.')