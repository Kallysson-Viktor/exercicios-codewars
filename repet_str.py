"""
Escreva uma função que aceite um número inteiro não negativo n e uma string s como parâmetros
e retorne uma string composta por s repetida exatamente n vezes.
"""
def repeat_str(repeat, string):
    resultado = repeat * string
    return resultado 

print(repeat_str(6, "Ola"))