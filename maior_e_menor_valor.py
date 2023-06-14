# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
denominador = 0
numerador = 0
maior_numero = 0
menor_numero = 0
r = ''
while r != 'S':
    
    numero = int(input('Digite um número: '))
    denominador += 1
    numerador += numero
    if numero > maior_numero:
        maior_numero = numero
    else:
        menor_numero = numero
    r = input('Deseja continua? S/N  ').upper()

media = numerador / denominador

if denominador == 1 and menor_numero == 0:
    menor_numero = numero

print(f'A média entre os {denominador} números digitados é de {media}.')
print()
print(f'O maior número foi {maior_numero}.')
print()
print(f'O menor número foi {menor_numero}.')