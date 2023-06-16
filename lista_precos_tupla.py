# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
# No final, mostre uma listagem de preços organizando os dados em forma tabular.

tupla = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Caderno', 18.00,
         'Estojo', 25.00,
         'Transferidor', 6.00,
         'Compasso', 10.00,
         'Mochila', 200.00,
         'Canetas', 30.00,
         'Livro', 35.00)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)


for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end='')
    else:
        print(f'R$ {tupla[pos]:>7.2f}')

print('-' * 40)