from emdereco1 import Cliente

cliente1 = Cliente('Wuelliton', 32)
cliente1.insere_endereco('Brasilia', 'DF')
print(cliente1.nome)
cliente1.lista_enderecos()
print()

cliente2 = Cliente('Jose', 22)
cliente2.insere_endereco('São Paulo', 'SP')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('Feli', 45)
cliente3.insere_endereco('Joinville', 'SC')
print(cliente3.nome)
cliente3.lista_enderecos()
print()


print('####################################################################')