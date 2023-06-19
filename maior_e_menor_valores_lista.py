# Faça um programa que leia 5 valores e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as
# suas respectivas posições na lista.


lista = [
    int(input('Digite o primeiro número: ')),
    int(input('Digite o segundo número: ')),
    int(input('Digite o terceiro número: ')),
    int(input('Digite o quarto número: ')),
    int(input('Digite o quinto número: '))
]

print(f'O maior valor digitado da lista foi: {max(lista)}')
print(f'O menor valor digitado da lista foi: {min(lista)}')
print(f'A posição do maior número é a {lista.index(max(lista))} e a posição do menor valor é a {lista.index(min(lista))}.')