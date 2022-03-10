def maximo(n1,n2):
    if n1 > n2:
        print(n1)
        return n1
    elif n2 > n1:
        print(n2)
        return n2
    else:
        print('son iguales')
        return n1

def vocal(letra):
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if letra in vocales:
        print('es una vocal')
    else:
        print('no es vocal')


vocal('E')