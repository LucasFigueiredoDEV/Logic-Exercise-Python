# Faça um progra,a que leia o ano de nascimento de um jovem, de acordo com a sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar
# Se já passou do tempo do alistamento.
# O programa também deverá mostrar o tempo que falta ou que passou do prazo.

print('\t Saiba quanto tempo falta para o seu alismento miltar')
print()

ano_nascimento = input('Digite o seu ano de nascimento: ')
ano_nascimento_int = int(ano_nascimento)
idade = 2023 - ano_nascimento_int
prazo = 18 - idade

if idade == 18:
    print('Já é a hora de alistar!')
elif idade < 18:
    print(f'Você ainda deverá que se alistar dentro de {prazo} anos.')
else:
    print('Já passou o seu tempo de alistamento, procure uma junta militar o mais rápido possível para resolver a sua situação!')