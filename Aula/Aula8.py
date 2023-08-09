'''
While em python
Utilizando para realizar ações enquanto
uma condição for verdadeira.
Requisitos: entender condições e operações
'''
'''Pergutando o nome da pessoa, sem parar!
while True: #loop infinito
    nome = input ("Qual e o seu nome? ")
    print(f'Olá {nome}!')
'''


'''x = 0
while x<100:
    if x == 3:
        x = x + 1
        break ##Vai para o codigo
        #continue##Vai continuar
    print(x)
    x = x + 1

print('Acabou!')'''


'''x = 0 #Coluna

while x < 10:
    y = 0 #Linha

    while y < 5:
        print (f'X vale {x} e Y vale {y}')
        y += 1

    x += 1 # x = x + 1
print('Acabou!')'''


while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro numero: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [S]im ou [N]ão: ')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric(): #Está verificando que o valor digitado for string, ira apresenta uma mensagem para digitar numero
        print('Você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador invalidor')

