# Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

while True:
    sexo = input('Digite o sexo:([M]asculino / [F]eminino)   ').upper()
    if sexo == 'M' or sexo == 'F':
        break
    else:
        print('Digite o valor novamente!')
    