# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores ordenada de forma descrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.


lista = []
while True:
    valores = int(input('Digite um número: '))
    lista.append(valores)
    saida = input('Deseja sair? S/N  ').upper()

    if saida == 'S' or saida == 'SAIR' or saida == 'SIM':
        break
    else:
        continue

print(f'Foram digitados {len(lista)} valores na lista.')
print(f'Os valores da lista em ordem decrescente: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 foi digitado e está na lista.')
else:
    print('O valor 5 não foi digitado e não está na lista.')