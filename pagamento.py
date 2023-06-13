# Elabora um programa que calcule o valor a ser pago por um produto
# considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão 20% de juros
import os

valor = input('Digite o valor do produto: ')
valor_float = float(valor)
while True:
    os.system('cls')
    print('\t FORMAS DE PAGAMENTO:')
    print('1 - À vista')
    print('2 - À vista no cartão')
    print('3 - Em 2x no cartão')
    print('4 - Em 3x ou mais no cartão')
    forma_pagamento = input('Digite o valor correspondente à sua forma de pagamento desejada: ')
    forma_pagamento_int = int(forma_pagamento)

    if forma_pagamento_int == 1:
        os.system('cls')
        print('\t Forma de pagamento selecinada: À vista/ Cheque')
        print('Essa forma de pagamento oferece 10% de desconto')
        desconto1 = valor_float - ((valor_float / 100) * 10)
        print(f'Valor original do produto: {valor_float}')
        print(f'Valor com desconto: {desconto1}')
        break
    elif forma_pagamento_int == 2:
        os.system('cls')
        print('\t Forma de pagamento selecionada: À vista no cartão')
        print('Essa forma de pagamento oferece 5% de desconto')
        desconto2 = valor_float - ((valor_float / 100) * 5)
        print(f'Valor original do produto: {valor_float}')
        print(f'Valor com desconto: {desconto2}')
        break
    elif forma_pagamento_int == 3:
        os.system('cls')
        print('\t Forma de pagamento selecionada: Em 2x no cartão')
        print(f'Valor a ser pago: {valor_float}')
        break
    elif forma_pagamento_int == 4:
        os.system('cls')
        print('\t Forma de pagamento selecionada: em 3x ou mais no cartão')
        print('Essa forma de pagamento acrescenta 20% de juros ao valor original do produto.')
        juros = valor_float + ((valor_float / 100) * 20)
        print(f'valor original do produto: {valor_float}')
        print(f'Valor do produto com acréscimo: {juros}')
        break
    elif forma_pagamento_int == 0:
        break
    else:
        print('Digite o valor de umas das opções d epagamento ou digite 0 para sair.')
        continue
