# Crie um módulo chamado moeda.py que tenha as funções incorpadas
# aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from modulos import moeda


p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13, True)}')

print()
print()
moeda.resumo(p, 10, 13)