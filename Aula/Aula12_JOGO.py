'''
Listas
fatiamento
append - inserir no final
insert - inserir
pop - remover 
del - deleta
clear - limpar
extendm, + - pode junta a duas listas
min, max
range
-----------------------
l1 = [1,2,3]
l2 = [4,5,6]
print(l2)
l2.insert(0,'banana')
print(l2)
del(l2[0])
print(l2)
l2.pop()
l2.append('b')

l1.extend(l2)

print(l1)
print(l2)
'''
## Esta tentando adivinha a palava segreta
secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len (letra) > 1:
        print('Ahh isso não vale, digite apenas letra.')

    
    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUULL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()
    
    segreto_temperario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            segreto_temperario += letra_secreta
        else:
            segreto_temperario += '*'
    if segreto_temperario == secreto:
        print(f'Que legal, VOCÊ GANHOUU!!!! A palabra era {segreto_temperario}')
        break
    else:
        print(f'A palavra secreta está assim: {segreto_temperario}')
    if letra not in secreto:
        chances -= 1
    
    print(f'Você ainda tem {chances} chances.')
    print()
