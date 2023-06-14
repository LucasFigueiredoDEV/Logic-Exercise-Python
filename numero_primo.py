# Faça um programa que leia um número e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))

for c in range (1, numero + 1):
    
    if numero % c == 0:
        print(f'\033[34m{c}')
    else:
        print(f'\033[m{c}')