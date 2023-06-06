#Escreva um procedimento que recebe as 3 notas de um aluno por parâmetro
#e uma letra. Se a letra for A o procedimento calcula a média aritmética das notas do aluno, se
#for P, a sua média ponderada (pesos: 5, 3 e 2) e se for H, a sua média harmônica.
# A média calculada também deve retornar por parâmetro.
import os
import sys


while True:
    print('A = Média aritmética')
    print('P = Média ponderada')
    print('H = Média armônica')
    tipo_media = input('Selecione seu tipo de média: ').lower()
    if tipo_media == 'a' or tipo_media == 'p' or tipo_media == 'h':
        os.system('cls')
        break
    elif tipo_media == 's':
        sys.exit()
    else:
        os.system('cls')
        print('A = Média aritmética')
        print('P = Média ponderada')
        print('H = Média armônica')
        print('Digite uma das opções ou digite "S" para sair do programa.')
        continue


while True:
    primeira_nota = input('Digite a sua primeira nota: ')
    segunda_nota = input('Digite a sua segunda nota: ')
    terceira_nota = input('Digite a sua terceira nota: ')
    primeira_nota_float = float(primeira_nota)
    segunda_nota_float = float(segunda_nota)
    terceira_nota_float = float(terceira_nota)


    if primeira_nota == '' or segunda_nota == '' or terceira_nota == '':
        print('Digite alguma coisa no campo.')
        continue
    elif primeira_nota == str or segunda_nota == str or terceira_nota == str:
        primeira_nota('Por favor digite valores númericos.')
        continue
    else:
        os.system('cls')
        break



def notas(nota1, nota2, nota3):
    if tipo_media == 'a':
        aritmetica = (nota1 + nota2 + nota3) / 3
        return aritmetica
    elif tipo_media == 'p':
        ponderada = ((nota1 * 5) + (nota2 * 3) + (nota3 * 2)) / 10
        return ponderada
    elif tipo_media == 'h':
        harmonica = 3 / ((1 / nota1) + (1/nota2) + (1/nota3))
        return harmonica

    
print(('Primeira nota: {}').format(primeira_nota))
print(('Segunda nota: {}').format(segunda_nota))
print(('Terceira nota: {}').format(terceira_nota))


print('A sua média é: {}'.format(notas(primeira_nota_float, segunda_nota_float, terceira_nota_float)))
        