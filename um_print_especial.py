# Faça um programa que tenha uma função chamada escreva(), que receba um texto
# qualquer como parâmetro e mostre uma mensagem como tamanho adaptável.

def escreva(msg):
    print('~' * len(msg))
    print(msg)
    print('~' * len(msg))

escreva('Olá, mundo!')
escreva('Programa desenvolvido por Lucas')