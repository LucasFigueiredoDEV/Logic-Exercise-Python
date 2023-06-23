# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los
# dentro da lista e a segunda função vai mostrar a soma entre todos
# os valores PARES sorteados pela função anterior.
from random import randint
from time import sleep


numeros = []


def sorteia():
    print(f'Sorteando 5 valores:', end='')
    for sorteia in range(0, 5):
        numero = randint(0, 10)
        numeros.append(numero)
        print(f'{numero}', end=' ', flush=True)
        sleep(1)


def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos valores pares sorteados é igual a {soma}')



sorteia()
print()
somapar(numeros)