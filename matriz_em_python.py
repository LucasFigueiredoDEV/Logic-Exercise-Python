# Crie um programa que crie uma matriz de dimensão 3x3
# e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[[0], [0], [0]],
         [[0], [0], [0]],
         [[0], [0], [0]]]
soma_par = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}] : '))
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
        
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()
for l in range(0, 3):
    soma_terceira_coluna += matriz[l][2]

for c in range(0, 3):
    if c == 0:
        maior_valor_segunda_linha = matriz[1][c]
    elif matriz[1][c] > maior_valor_segunda_linha:
        maior_valor_segunda_linha = matriz[1][c]




print(f'A soma dos valores pares digitados é igual a {soma_par}')
print(f'A soma dos valores da terceira coluna é igual a {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_valor_segunda_linha}')