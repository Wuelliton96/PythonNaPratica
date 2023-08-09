'''
sets(conjuntos)
add(adiciona), update(atualiza), clear(limpa), discard(remover)
uniom | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
'''
l1 = ['Luiz', 'Joao','Maria']
l2 = ['Joao', 'Maria', 'Maria',
     'Luiz', 'Luiz', 'Luiz', 'Luiz', 'Luiz', 'Luiz', 'Luiz']

l1 = list(set(l1))
l2 = list(set(l2))

print(l1, l2)

if set(l1) == set(l2):
    print('L1 é igual a L2')
else: 
    print('L1 é diferente de L2')