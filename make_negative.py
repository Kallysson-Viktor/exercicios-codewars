"""
Nesta tarefa simples, você recebe um número e tem que torná-lo negativo.
Mas talvez o número já seja negativo? O número já pode ser negativo, caso em que nenhuma 
alteração é necessária.
"""
def make_negative( number ):
    #O abs() remove o sinal do número, deixando-o positivo, e o - na frente transforma em negativo.
   return - abs(number) 
   

print(make_negative(7))

