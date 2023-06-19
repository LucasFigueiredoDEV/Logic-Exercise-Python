# Crie um programa onde o usúario possa sigitar vários valores numéricos e cadastreos em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
    valores = int(input('Digite um número: '))
    saida = input('Deseja sair? S/N  ').upper()

    if valores not in lista:
        lista.append(valores)


    if saida == 'S' or saida == 'SIM':
        break
    else:
        continue

print(f'Os valores da lista em ordem crescente são: {sorted(lista)}')