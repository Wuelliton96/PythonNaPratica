'''
Sistema de pergunta
'''
print()
print('Texto Explicativo')

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {'a': '1','b': '4', 'c': '5',},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 5 * 3?',
        'respostas': {'a': '15','b': '14', 'c': '55',},
        'resposta_certa': 'a',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 7 * 3?',
        'respostas': {'a': '21','b': '24', 'c': '22',},
        'resposta_certa': 'c',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 5 / 5?',
        'respostas': {'a': '1','b': '0', 'c': '5',},
        'resposta_certa': 'a',
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 15 + 0?',
        'respostas': {'a': '0','b': '15', 'c': '1',},
        'resposta_certa': 'b',
    },
}

print()
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    
    print('Alternativas:')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('EHHHHHHH!!! VoCçe acertou!!!!')
        respostas_certas += 1
    else:
        print('Ixiiiiii!!! Você ERRRRROOUU!!!!')
    print()

qtd_perguntas = len(perguntas)
porcetagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} de {qtd_perguntas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcetagem_acerto}%')
