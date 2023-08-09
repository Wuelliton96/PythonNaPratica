'''
Funções (def) -  return
'''

def f(var):
    print(var)

def dumb():
    return f

var = dumb()
print(type(var))

if var == f:
    print('var é igual a f')
else:
    print('Blaaaaaaaa')