# Desenvolva uma logica que leia o peso e a altura de uma pessoa
# Calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade morbida
import os
print('\t Vamos calcular o seu IMC')
print()

peso = input('Digite o seu peso em Kg: ')
altura = input('Digite a sua altura: ')

peso_float = float(peso)
altura_float = float(altura)

imc = peso_float/ (altura_float ** 2)
os.system('cls')

if imc < 18.5:
    print(f'Seu IMC é {imc:.2f} e é considerado abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é {imc:.2f} e é condiderado como peso ideal.')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é {imc:.2f} e é considerado sobrepedo.')
elif imc >= 30 and imc < 40:
    print(f'Seu IMC é {imc:.2f} e é considerado como Obesidade')
else:
    print(f'Seu IMC é {imc:.2f} e é considerado como obesidade morbida')
