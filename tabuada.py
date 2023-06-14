# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    valor = int(input('Digite o valor que vôce deseja ver a tuabuada: '))
    if valor >= 0:
        print('-=' * 15)
        for c in range(0, 11):
            multiplicacao = valor * c
            print(f'\t{valor} x {c} = {multiplicacao}')
        
        print('-=' * 15)
    else:
        break

print('FIM!')