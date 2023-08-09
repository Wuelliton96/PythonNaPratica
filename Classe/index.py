'''
Associação

'''
from Classe.index1 import Escrito
from Classe.index1 import Caneta
from Classe.index1 import MaquinaDeEscrever

escrito = Escrito('Wuelliton')
caneta =  Caneta('Bic')
maquina = MaquinaDeEscrever()

print(escrito)

escrito.ferramenta = maquina
escrito.ferramenta.escrever()

