# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função.


def notas(*nota, sit = False):
    """
    -> Função para analisar notas e situações de alunos
    :param nota: Uma ou mais notas dos alunos (Aceita várias).
    :param sit: valor opcinal, indicando se deve ou não aceitar a situação.
    :return: dicionário com várias informações sobre a situação da turma
    """
    maior_nota = max(nota)
    menor_nota = min(nota)
    
    soma_notas = sum(nota)
    

    
    media = soma_notas/ len(nota)
    
    
    situacao_tuma = ''
    if media < 6:
        situacao_tuma = 'RUIM'
    elif media >= 6 and media < 7:
        situacao_tuma = 'RAZOÁVEL'
    else:
        situacao_tuma = 'BOA'
    

    dicionario = {'Quantidade de notas': len(nota),
                  'Maior nota': maior_nota,
                  'Menor nota': menor_nota,
                  'Média da turma': media}
    
    
    if sit == True:
        dicionario['Situação'] = situacao_tuma
    
    
    return dicionario



print()
print(notas(5, 6, 10, 0, 0, 8, sit=True))
print()
