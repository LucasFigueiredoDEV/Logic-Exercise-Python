# O computador vai "pensar" em um número entre 0 e 10. Só vai tentar 
# adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
import os

from random import randint

computador  = randint(0, 10)
contador = 0

while True:
    print('\tAdivinhe o número de 1 a 10 que o computador está pensando!')
    jogada = int(input('Digite o número que o computador está pensando: '))

    if jogada == computador:
        break
    else:
        contador += 1
        os.system('cls')
        print('Valor errado, tente novamente!')
        continue
os.system('cls')
print('Você venceu!')
print(f'O número que o computador estava pensando era o {computador}.')
print(f'Foram necessárias {jogada} jogadas para que você vencesse!')