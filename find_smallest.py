"""
Dada uma matriz de inteiros, sua solução deve encontrar o menor inteiro.
"""
def find_smallest_int(arr):
        menor_atual = arr[0] #inicializei o menor atual com o indice da lista, se fosse com 0 iria dar erro por ter numeros negativos 

        for numero in arr:
                if numero < menor_atual:
                 menor_atual = numero 
        return menor_atual
input_list = [34, -345, -1, 100]
print(find_smallest_int(input_list))
