'''
Formatando valores com modificadores
:s - Texto (strings)
:d - Inteiros (int)
:f - numeros de flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> OU < OU ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda acrecentando
< - Direita acrecentando
^ - Centro acrecentando
'''
num_1 = 10
num_2 = 3

divisao = num_1 / num_2
print(f'{divisao:.2f}')

print(f'{num_1:0>10}')
print(f'{num_2:0>10.2f}')

nome = 'Wuelliton'
sobrenome = 'Santos'
nome_formatado = '{0:$^15} {1:+^15}'.format(nome, sobrenome)
print(nome_formatado)


print(nome.lower())#tudo minusculo
print(nome.upper())#tudo maiusculo
print(nome.title())#primeira letra maiusculas