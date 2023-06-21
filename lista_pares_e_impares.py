# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
# lista única que mantenha separados os valores pares e ímpares.
# No final mostre os valores pares e ímpares em ordem crescente.


lista_unica = [[], []]


for valores in range(0, 7):
    valor = int(input('Digite o valor: '))
    if valor % 2 == 0:
        lista_unica[0].append(valor)
    else:
        lista_unica[1].append(valor)

for ordem in lista_unica:
    crescente_par = sorted(lista_unica[0])
    crescente_impar = sorted(lista_unica[1])

print(f'Os valores pares em ordem crescente são: {crescente_par}')
print(f'Os valores ímpares em ordem crescente são: {crescente_impar}')