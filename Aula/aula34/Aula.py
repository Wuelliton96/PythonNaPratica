from aula34 import preco

def aumento(valor, porcentagem, formata = False):
    r= valor + (valor * (porcentagem / 100))

    if formata:
        return preco.real(r)
    else:
        return r

def re(valor, porcentagem, formata = False):
    r = valor - (valor * (porcentagem / 100))

    if formata:
        return preco.real(r)
    else:
        return r