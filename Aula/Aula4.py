'''
Operadores Relacionais
== igualdade
> maior que
>= maior que ou igual a
< menor que
<= menor que ou igua a
!= diferente
'''
nome = input("Qual e o seu nome? ")
idade = input(" Qual a sua idade? ")

idade = int(idade)

#limite para pega empréstimo
idade_menor = 18 #jovem
idade_maior = 30 #passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO  pode pegar o empréstimo.')