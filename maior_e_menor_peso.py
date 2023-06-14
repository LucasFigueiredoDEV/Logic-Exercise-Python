# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual
# foi o maior e o menor peso lidos.
maior_peso = 0
menor_peso = 0
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}ª pessoa em KG: '))
    if p == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso
print(f'O maior peso é {maior_peso} Kg')
print()
print(f'O menor peso é {menor_peso} Kg')

