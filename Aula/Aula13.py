'''
For / Else
'''
variavel = ['Wuelliton Santos', 'João Marcos', 'Ines']

for valor in variavel:
    if valor.lower().startswith('j'):
        continue
    print(valor)