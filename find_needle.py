"""Escreva uma função `findNeedle()` que receba um array cheio de itens irrelevantes, mas que contenha
uma "agulha". Depois que sua função encontrar a agulha, ela deve retornar uma mensagem (como uma string)
que diz: "encontrou a agulha na posição " mais o índice onde a agulha foi encontrada, então: deve retornar 
"found the needle at position 6
"""
def find_needle(haystack):
    palavra_buscada = "needle"
    for indice, elemento in enumerate(haystack):
        if elemento == palavra_buscada:
            return f"found the needle at position {indice}"

lista = ["hay", "junk", "hay", "hay", "moreJunk", "randomJunk", "needle"]
print(find_needle(lista))