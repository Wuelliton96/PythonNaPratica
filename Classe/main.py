'''
Metodos de classes -  são metodos relativos a classe inteira.
Metodos de estativo - são metodos estaticos
'''
from random import randint

class Pessoa:
    ano_atual = 2019
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
            print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod
    def gera_id():
         rand = randint(100000, 19999)
         return rand

p1 = Pessoa('Wuelliton', 32)
p1 = Pessoa.por_ano_nascimento('Wuelliton', 1987)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id)

