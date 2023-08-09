'''
Funções - def
'''

def saudacao(msg='elá', nome='usuário'):
    nome = nome.replace('e','3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'
variavel = saudacao()

print(variavel)