# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
execucao = 0
while execucao != 5:
    numero1 = float(input('Digite um número: '))
    numero2 = float(input('Digite um segundo número: '))
    while execucao != 5:
        
        print('''
        [1] somar
        [2] multiplicar
        [3] maior
        [4]novos números
        [5] sair do programa''')
        execucao = int(input('Digite a opção selecionada: '))

        if execucao == 1:
            soma = numero1 + numero2
            print(f'RESULTADO DA SOMA: {soma}')
        elif execucao == 2:
            multiplica = numero1 * numero2
            print(f'RESULTADO DA MULTIPLICAÇÃO: {multiplica}')
        elif execucao == 3:
            if numero1 > numero2:
                print(f'O número {numero1} é maior que o número {numero2}.')
            elif numero2 > numero1:
                print(f'O número {numero2} é maior que o número {numero1}.')
            else:
                print('Não existe número maior, os dois números possuem o mesmo valor!')
        elif execucao == 4:
            break

print('FIM!')
            
