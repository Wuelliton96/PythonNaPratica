'''
While / Else
Contadores
Acumuladores
'''
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no Else.')
print('Passei do else após o break ser executado, saindo fora do laço')