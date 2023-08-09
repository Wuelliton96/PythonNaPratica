'''
Dicionarios
'''
cliente = {
    'cliente1' : {
        'nome': 'Wuelliton',
        'sobrenome':'Santos'
    },
    'cliente2' : {
        'nome': 'Brenda',
        'sobrenome':'Santos'
    },
}

for clientes_k, clientes_v in cliente.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')