# Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de três
# e que se encontram no intervalor de 1 até 500
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print(f'A soma de todos {cont} os valores impares e multiplos de três é {s}')
    