'''
Levantando exceções
https://docs.python.org/3/library/exceptions.html
'''
def divide(n1, n2):
    if n2 == 0:
        if n2 == 0:
            raise ValueError("N2 bão pode ser 0.")
    return n1 / n2
try:
    print(divide(n1=2,n2=0))
except ValueError as error:
    print('Você está tentando dividir por 0.')
    print('Log: ',error)
