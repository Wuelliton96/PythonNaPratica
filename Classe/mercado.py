from Classe.mercado1 import CarrinhoDeCompras, Produto

carinho = CarrinhoDeCompras()

p1 = Produto('Camisa', 50)
p2 = Produto('Notbook', 150)
p3 = Produto('Carregados', 550)
p4 = Produto('Pc', 450)
p5 = Produto('Teclado', 510)

carinho.inserir_produto(p1)
carinho.inserir_produto(p2)
carinho.inserir_produto(p2)
carinho.inserir_produto(p3)
carinho.inserir_produto(p3)
carinho.inserir_produto(p4)

carinho.lista_produto()
print(carinho.soma_total())



