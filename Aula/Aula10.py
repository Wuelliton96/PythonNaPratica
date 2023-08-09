'''
Iterando strings com while
'''
while True:
    minha_string = input('Digite uma frase: ')
    tamanho_string = len(minha_string)

    print(minha_string.count('a'))#como saber a letra A ocorreu dentro da frase.

    c = 0
    contagem_atual = 0 
    letra = ''
    nova_string = ''

    while c < tamanho_string:
        qtd_vezes_letra = minha_string.count(minha_string[c])#Verificando a quantidade de letras que se repete

        if contagem_atual < qtd_vezes_letra and minha_string[c].strip():#verificando repitição
            letra = minha_string[c]
            contagem_atual = qtd_vezes_letra

        if minha_string[c] == 'r':
            nova_string = nova_string + minha_string[c].upper()
        else:
            nova_string = nova_string + minha_string[c]
        #print(nova_string)#Como você saber de como esta sendo montado
        c += 1
    print(letra, contagem_atual)
    print(nova_string)

'''
string = 'valor'
c=0
while c < len(string):
    print(string[c])
    c += 1
'''