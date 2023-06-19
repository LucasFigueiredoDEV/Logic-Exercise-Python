# Crie um programa onde o usúario possa digitar 5 valores e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
lista = []
for valor in range(5):
    valores = int(input('Digite o valor: '))
    if valor == 0 or valores > lista[-1]:
        lista.append(valores)
    else:
        pos = 0
        while pos < len(lista):
            if valores <= lista[pos]:
                lista.insert(pos, valores)
                break
            pos += 1
            

print(f'Os valores presentes na lista são: {lista}')