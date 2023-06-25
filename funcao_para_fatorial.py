# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# O primeiro que indique o número a calcular e o outro chamado show, que será opcional
# que será um valor lógico (opcional) indicando se será mostrando ou não na tela o processo de calculo do fatorial.


def fatorial (numero, show=False):
    f = 1
    for c in range(numero, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
        
    
        

print('~'*30)
print(fatorial(5))
print('~'*30)
