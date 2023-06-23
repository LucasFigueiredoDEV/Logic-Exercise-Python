# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada.
from time import sleep

def contador(inicio, fim, passo):
    
    for c in range(inicio, fim, passo):
        print(c)
        sleep(1)



print('Contagem de 1 até 10, de 1 em 1:')
for c in range(1, 11):
    print(c)
    sleep(1)



print()
print('Contagem de 10 até 0, de 2 em 2:')
for c in range(10, -1, -2):
    print(c)
    sleep(1)



print()
print('Agora é a sua vez de personalizar a contagem!')
start = int(input('Início: '))
end = int(input('Fim: '))
step = int(input('Passo: '))

contador(start, end, step)