"""
Escreva uma função `partlist` que forneça todas as maneiras de dividir uma lista (um array) de pelo menos dois elementos em duas partes não vazias.
Cada par de partes não vazias será representado como um par (ou um array para linguagens sem tuplas, ou uma `struct` em C — veja os exemplos de casos de teste para C).
Cada parte será representada como uma string.
Os elementos do par devem manter a mesma ordem da lista original.
"""
def partlist(arr):
    resultado = []
    separador = " "

    for corte in range(1, len(arr)): #O len(arr) retorna a quantidade de elementos da lista.    
        primeira_parte = arr[:corte]
        segunda_parte = arr[corte:]

        primeira_string = separador.join(primeira_parte) #O join() transforma a primeira parte, que ainda é uma lista, em uma string
        segunda_string = separador.join(segunda_parte) #O exercício exige que cada parte seja uma string, por isso usamos o join().

        tupla = (primeira_string, segunda_string)
        resultado.append(tupla)
    return resultado 

a = ["az", "toto", "picaro", "zone", "kiwi"]
print(partlist(a))

