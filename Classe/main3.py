'''
Encapsulamento
public - São metodos e atributos que podem se acessado dentro e fora da classe
protected - Apenas dentro da classe ou da filha
private - so esta disponivel somente na classe
_  é private simples ou protected (pulico)
__ total private(_NOMECLASSE__NOMEATRIBUTO)
'''

class BaseDedados:
    def __init__(self):
        self.__dados = {}
    
    @property
    def __dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)


    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDedados()
bd.inserir_cliente(1, 'Wuelliton')
bd.inserir_cliente(2, 'Santos')
bd.inserir_cliente(3, 'Dado')
bd.inserir_cliente(4, 'Wuelliton')
bd.apaga_cliente(4)
bd.lista_clientes()

print(bd.__dados)