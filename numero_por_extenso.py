# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 
'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    escolha_usuario = int(input('Escolha um número de 0 a 20: '))


    if escolha_usuario < 0 or escolha_usuario > 20:
        print('Tente novamente!')
        continue
    else:
        break

print(numeros[escolha_usuario])