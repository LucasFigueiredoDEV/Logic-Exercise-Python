# Crie um prograna que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a 
# condição de parada. No final, mostre quantos números fora digitados e qual 
# foi a soma entre eles (desconsiderando o flag).
soma = 0
contagem = 0
valor = 0
while valor != 999:
    valor = int(input('Digite um valor: '))
    
    if valor != 999:
        soma += valor
        contagem += 1

print(f'{contagem} Números foram lidos e {soma} é o resultado da soma entre eles.')