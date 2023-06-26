# Reescreva a função leiaint() que foi feita no desafio "Validando entrada de dados em python",
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiafloat() com a mesma funcionalidade.


def leiaint(num):
    while True:
        try:
            valor = int(input(num))
        except Exception as erro:
            print(f'Ocorreu um erro do tipo {erro.__class__}')
            print('Por favor digite um número inteiro.')
            continue
        else:
            print(f'O valor digitado foi o {valor}')
            break
        


def leiafloat(num):
    while True:
        try:
            valor = float(input(num))
        except Exception as erro:
            print(f'Ocorreu um erro do tipo {erro.__class__}')
            print('Por favor digite um número de ponto flutuante.')
            continue
        else:
            print(f'O valor digitado foi o {valor}')
            break


leiaint('Digite um número inteiro: ')
leiafloat('Digite um número de ponto flutante: ')
            