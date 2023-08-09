'''
Manipulando strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:
    http://docs.python.org/3/library/stdtypes.html (tipos built-in)
    http://docs.python.org/3/library/functions.html (funções built-in)

'''
#positivos     [012345678]
texto     =    'Python s2' 
#negativos    -[987654321]

url = 'www.google.com.br/'

nova_string = texto[2:6]

print(len(texto))

for letra in texto:
    print(letra)

print(nova_string)
print(url[:-1])
print(texto[8])