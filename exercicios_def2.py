"""
Crie uma função chamada notas_aprovadas que receba uma lista de notas (lista de floats) e retorne uma lista apenas com as notas maiores
ou iguais a sete.
"""
def notas_aprovadas(lista_notas):
    lista_aprovados = []

    for notas in lista_notas:
        if notas >= 7:
            lista_aprovados.append(notas)

    return lista_aprovados

lista_notas_alunos = [10.0, 7.5, 6.9]
lista_resultante = notas_aprovadas(lista_notas_alunos)

print("Notas Aprovados")
print(lista_resultante)
