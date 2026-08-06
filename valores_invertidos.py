""""
Dado um conjunto de números, retorne o inverso aditivo de cada um. Cada positivo se torna negativo, 
e os negativos se tornam positivos.
"""
def invert(lst):
    lista_invertida = [] # criei uma lista vazia para ele ia adicionando com o append os numeros invertidos
    for numero in lst:
        if numero > 0:
         lista_invertida.append(-abs(numero))
        else:
         lista_invertida.append(abs(numero))
    return lista_invertida


lista = [1, 2, 3, 4, 5] 
negative_list = [1, -2, 3, -4, 5] 

print(invert(lista))
print(invert(negative_list))
