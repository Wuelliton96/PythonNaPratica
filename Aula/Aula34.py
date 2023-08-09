'''
Criando pacotes
'''

#import aula34.Aula
#from aula34 import Aula

from aula34.Aula import aumento, re
from aula34.Aula import preco as preco2

preco = 49.90
preco_com_aumento = aumento(preco,15, formata=True)
print(preco_com_aumento)

preco_com_reducao = re(preco,15, formata=True)
print(preco_com_reducao)

print(preco2.real(59,99))