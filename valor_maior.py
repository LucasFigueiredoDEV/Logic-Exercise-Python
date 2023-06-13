# Escreva um programa que leia dois números e compare-os mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

print('\tComparando dois valores inteiros')
print()
numero1 = input('Digite o primeiro valor inteiro: ')
numero1_int = int(numero1)

numero2 = input('Digite um segundo valor inteiro: ')
numero2_int = int(numero2)

if numero1_int > numero2_int:
    print('O primero valor é maior!')
elif numero2_int > numero1_int:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais!')
