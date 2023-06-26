def aumentar(valor, porc, p = False):
    porcentagem = (valor / 100) * porc
    valor_aumentado = valor + porcentagem
    if p == True:
        return moeda(valor_aumentado)
    return valor_aumentado


def diminuir(valor, porc, p = False):
    porcentagem = (valor / 100) * porc
    valor_reduzido = valor - porcentagem
    if p == True:
        return moeda(valor_reduzido)
    return valor_reduzido


def dobro(valor, p = False):
    dobrando = valor * 2
    if p == True:
        return moeda(dobrando)
    return dobrando

def metade(valor, p = False):
    dividindo = valor / 2
    if p == True:
        return moeda(dividindo)
    return dividindo


def moeda(msg):
    return f'R${msg:.2f}'.replace('.', ',')


def resumo(msg, valor_aumento, valor_reduz):
    print('-' * 30)
    print('\tRESUMO DO VALOR')
    print('-' * 30)
    print(f'Preço analisado: {moeda(msg)}')
    print(f'Dobro do preço: {dobro(msg, True)}')
    print(f'Metade do preço: {metade(msg, True)}')
    print(f'{valor_aumento}% de aumento: {aumentar(msg,valor_aumento, True)}')
    print(f'{valor_reduz}% de redução: {diminuir(msg,valor_reduz, True)}')
    print('-' * 30)