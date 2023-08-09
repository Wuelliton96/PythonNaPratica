'''
Operadores lógicos
and, or, not
in Ele ira encontrar algo na variavel
not in ele não estive dentro da variavel

(verdadeiro E false) = falso
comparacao1  and comparacao

(verdadeiro OU verdadeiro)
comp1 OR comp2 

not ele demonstra que ele não tem nada prenchido.
a = ''
b = 0
if not b:
    print('Por favor, preencha o valor de B.')

'''

usuario =  input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'wuelliton'
senha_bd = '123456'

if usuario_bd == usuario and usuario_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos.')