#Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o seu volume (v = 4/3.P .R3)

valor_raio = input('Qual o valor do raio da esfera? ')
valor_raio_float = float(valor_raio)

def calcular(valor_raio_float):
    volume = float(4/3 * 3.14)
    calculando = volume * (valor_raio_float**3)
    return calculando

print('Valor do raio: {}'.format(calcular(valor_raio_float)))