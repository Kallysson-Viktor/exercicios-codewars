# separador = "/"
# minha_lista = ["Azul", "Amarelo", "Laranja"]
# string_resultante = separador.join(minha_lista)

# print(string_resultante)
# print(type(string_resultante))
# ============================
# # posicoes          0           1           2         3        4
# minha_lista = ["Brasil", "Argentina", "Colômbia", "Peru", "Bolívia"]

# primeiro_pedaco = minha_lista[:2]
# print(f"Primeiro pedaço: {primeiro_pedaco}")

# segundo_pedaco = minha_lista[2:]
# print(f"Segundo pedaço: {segundo_pedaco}")
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
