'''
List comprehension
'''

l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]

ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]

l2 = ['Wuelliton', 'Rodrigo', 'Iago']
ex4 = [v.replace('i', '@') for v in l2]
print(ex4)

tupla = (
    ('chave1', 'valor1'),
    ('chave', 'valor')
)

ex5 = [(y, x) for x, y in tupla]
ex5 = dict(ex5)
print(ex5['valor1'])

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
print(ex6)

ex7 = [v if v % 3 == 0 and v % 8 == 0 else 'Não é' for v in l3]
print(ex7)