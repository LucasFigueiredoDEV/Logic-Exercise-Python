# Crie um programa que leia duas notas de um aluno e calcule a sua média,
# mostrando no final, de acordo com a média atingida;
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERACÃO
# Média 7.0 ou superior: APROVADO

print('\tVamos calcular a sua média!')
print()
nota1 = input('Digite a sua primeira nota: ')
nota2 = input('Digite a sua segunda nota: ')

nota1_float = float(nota1)
nota2_float = float(nota2)

media = (nota1_float + nota2_float) / 2

if media < 5.0:
    print('REPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')