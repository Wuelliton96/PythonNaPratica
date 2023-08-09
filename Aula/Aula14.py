'''
Split, Joinm, Enumerate
* Split - Dividir uma string #str
* Join - Juntar uma lista #str
* Enumerate - Enumerar elementos da lista #iteráveis
________________________________________________________
string = 'O Brasil é o pais do futebol, o brasil é penta'
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mas vezes é {palavra} ({contagem}x)')
____________________________________________________________________
string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = ','.join(lista)

print(string)
print(lista)
print(string2)
'''
string = 'O brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor)