# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50
print('\t Os números pares entre 1 e 50 são:')
for c in range(1, 51):
    pares = c % 2
    if pares == 0:
        print(c)
