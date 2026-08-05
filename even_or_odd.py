"""
Crie uma função que receba um número inteiro como argumento e retorne "Even" para números 
pares ou "Odd" para números ímpares.
"""
def even_or_odd(x):
    number = x
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("EVEN OR ODD")

x = int(input("Digite um número: "))
resultado = even_or_odd(x)

print(resultado)

    