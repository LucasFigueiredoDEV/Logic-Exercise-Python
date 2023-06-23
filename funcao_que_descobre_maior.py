# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
# com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep



def maior(*numeros):
    cont = 0
    maior = 0

    print('Analisando os valores enviados...')
    for valor in numeros:
        print(f'{valor} ', end='', flush=True)
        sleep(0.8)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    
    print()
    print(f'Foram enviados {cont} valores, e o maior valor entre os enviados é o {maior}.')



maior(1, 2, 3, 4, 10)