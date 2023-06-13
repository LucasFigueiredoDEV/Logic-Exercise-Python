# Escreva um programa para aprovar o empréstimo
# bancário para a compra de uma casa. O programa vai perguntar
# o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%
# do salário ou então o esmpréstimo será negado.
import os
print('\tFORMULÁRIO')
print()

nome = input('Digite o seu nome: ')
os.system('cls')
   
print('\tFORMULÁRIO')
print(f'Olá, Senhor(a) {nome}, iremos te fazer mais algumas perguntas!')
print()
valor_casa = input('Digite o valor da casa: ')
valor_casa_float = float(valor_casa)

salario = input('Digite o valor do seu salário: ')
salario_float = float(salario)

anos = input('Digite em quantos anos deseja pagar a casa: ')
anos_int = int(anos)
    
prestacao_mensal = valor_casa_float / (anos_int * 12)
trinta_porc_salario = (salario_float / 100) * 30

if prestacao_mensal > trinta_porc_salario:
    print('Empréstimo negado!')
else:
    print('Emprestimo aprovado!')