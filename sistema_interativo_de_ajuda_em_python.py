# Faça um mini-sistema que utilize o interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuáriio digitar a palavra 'FIM', o programa se encerrará.
# OBS: use cores.
from time import sleep

def ajuda(com):
    titulo(f'Acessando o manual do comando {com}.')
    help(com)
    sleep(2)


def titulo(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
print('ATÉ LOGO!')


