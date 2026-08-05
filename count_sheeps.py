"""
Considere uma matriz/lista de ovelhas onde algumas ovelhas podem estar faltando em
 seu lugar. Precisamos de uma função 
que conte o número de ovelhas presentes na matriz (verdadeiro significa presente).
"""
def count_sheeps(sheep):
    contador = 0
    for item in sheep:
        if item == True:
            contador += 1
    return contador

lista_ovelhas = [
    True,  True,  True,  False,
    True,  True,  True,  True ,
    True,  False, True,  False,
    True,  False, False, True ,
    True,  True,  True,  True ,
    False, False, True,  True
]   
print(count_sheeps(lista_ovelhas))
