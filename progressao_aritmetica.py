# Desenvolva um programa que leia o primeiro termo e a razão de uma
# Progressão aritmética. No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite o valor da razão: '))

for c in range(0, 10):
    primeiro_termo += razao
    print(primeiro_termo)