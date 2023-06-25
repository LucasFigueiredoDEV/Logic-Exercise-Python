# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante
# à função input() do Python, só que fazendo a validação para aceitar apenas valor numérico.
# Ex: n = leiant('Digite um n')


def leiaint(numero):
    while True:
        valor = str(input(numero))
        if valor.isnumeric():
            print(f'O número digitado foi o {valor}.')
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro.\033[m')
            continue
        

        



num = leiaint('Digite um número: ')