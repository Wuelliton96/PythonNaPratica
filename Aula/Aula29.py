'''
Geradores, iteradores e iteráveis
'''

l1 = [x for x in range(10000)]
l2 = (x for x in range(10000))

for v in l2:
    print(v)