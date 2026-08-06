"""
Na reunião anual de família, a família gosta de encontrar a idade do membro da família vivo mais velho
e a idade do membro mais jovem da família e calcular a diferença entre eles.
Você receberá uma variedade de todas as idades dos membros da família, em qualquer ordem. As idades serão 
dadas em números inteiros, portanto, um bebê de 5 meses terá uma 'idade' atribuída de 0. Retorna uma nova 
matriz (uma tupla em Python) com [idade mais jovem, idade mais velha, diferença entre a idade mais jovem e a 
mais velha].
"""
def difference_in_ages(ages):
    mais_velho = ages[0]
    mais_jovem = ages[0]

    for idade in ages:
        if idade < mais_jovem:
            mais_jovem = idade
        if idade > mais_velho:
            mais_velho = idade
    diferenca = mais_velho - mais_jovem
    tupla = (mais_jovem, mais_velho, diferenca)
    return tupla
lista_idades = [16, 22, 31, 44, 3, 38, 27, 41, 88]
print(difference_in_ages(lista_idades))

lista_idades = [33, 33, 33]
print(difference_in_ages(lista_idades))

    