# Cie um programa que simule o funcionamento de um caixa eletrônco.
# No início, pergunte ao usuário qual será o valor
# a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possue cédulas da R$ 50, R$20, R$10 e R$1.


cedula = 50
saque = int(input('Digite o valor que deseja sacar: '))
total = saque
totced = 0
while True:
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} de cédulas de R${cedula}')
        
        
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0


        if total == 0:
            break
    

