# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = []
while True:
    valor = int(input('Digite um número: '))
    lista.append(valor)

    saida = input('Deseja sair? S/N  ').upper()

    if saida == 'S' or saida == 'SIM' or saida == 'SAIR':
        break
    else:
        continue
lista_par = []
lista_impar = []

for valores in lista:
    if valores % 2 == 0:
        lista_par.append(valores)
    else:
        lista_impar.append(valores)

print(f'Os valores da primeira lista são: {lista}')
print()
print(f'Os valores da "Lista par" são: {lista_par}')
print()
print(f'Os valores da "Lista impar" são: {lista_impar}')
