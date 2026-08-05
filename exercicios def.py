"""
Crie uma função chamada
calcular_velocidade_media que receba a distância percorrida (em km) e o
tempo gasto para o deslocamento (horas). A função deve calcular a velocidade média e
devolvê-la arredondada com duas casas decimais.
"""

def calcular_velocidade_media(distancia, tempo):
    resultado = distancia / tempo 
     #A função round(número, casas) pega o valor calculado e o arredocasas decimais.
    resultado = round(resultado, 2)
     #O return devolve o valor pronto para quem chamou a função. Sem o return, o cálculo seria feito, mas o resultado se perderia na memória.
    return resultado 

dist = float(input("Informe a distância (km): ")) 
tempo = float(input("Informe o tempo (h): "))
vel_média  = calcular_velocidade_media(dist, tempo)

print(f"Velocidade média: {vel_média}km/h")