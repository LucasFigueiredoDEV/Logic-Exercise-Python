# Escreva um programa que leia um número na tela os n primeiros elementos de uma sequência de Fibonacci
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
numero = int(input('Digite quantas sequências de Fibonacci você quer mostrar: '))

contagem = 3
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} -> {t2} ', end= '')
while contagem <= numero:
    t3 = t1 + t2
    print(f'-> {t3} ', end='')
    t1 = t2
    t2 = t3
    contagem += 1
    
print('-> FIM')