"""
====================================================================
PROGRAMA: Cálculo e Classificação de IMC (Índice de Massa Corporal)
====================================================================
DESCRIÇÃO:
Este programa solicita ao usuário o seu peso (em kg) e a sua altura 
(em metros). A partir desses dados, ele calcula o IMC através da 
fórmula: IMC = Peso / (Altura²) e exibe a categoria correspondente.

TABELA DE CLASSIFICAÇÃO UTILIZADA:
- IMC menor que 17:             Muito abaixo do peso
- IMC entre 17.0 e 18.49:       Abaixo do peso
- IMC entre 18.5 e 24.99:       Peso ideal
- IMC entre 25.0 e 29.99:       Sobrepeso
- IMC entre 30.0 e 34.99:       Obesidade
- IMC entre 35.0 e 39.99:       Obesidade Severa
- IMC maior ou igual a 40.0:    Obesidade Mórbida
====================================================================
"""
m = float(input("Massa(KG): "))
a = float(input("Altura(M): "))

imc = m / (a ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 17 :
    print("Você está muito abaixo do peso ")
elif imc >= 17 and imc < 18.5:
    print("Você está abaixo do peso ")
elif imc >= 18.5 and imc < 25 :
    print("PESO IDEAL ")
elif imc >= 25 and imc < 30 :
    print("Você está com sobrepeso ")
elif imc >= 30 and imc < 35 :
    print("Você está com obesidade ")
elif imc >= 35 and imc < 40 :
    print("Você esta com Obesidade Severa ")
else:
    print("Você está com Obesidade Mórbida ")