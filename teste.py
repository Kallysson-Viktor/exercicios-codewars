""""
Crie uma função chamada media_aluno que receba como parâmetro o identificador do aluno
Entrada de dados: Solicitar que o usuário digite três notas float referentes àquele aluno.
Processamento: Calcular a média aritmética das três notas e arredondá-la para uma casa decimal usando a função nativa round().
Saída: Imprimir uma mensagem formatada na tela mostrando o número do aluno recebido por parâmetro e a média calculada.
"""
def media_aluno(numero_aluno):
    nota1 = float(input("Qual a primeira nota?  "))
    nota2 = float(input("Qual a segunda nota? "))
    nota3 = float(input("Qual a terceira nota? "))

    media = (nota1 + nota2 + nota3) / 3 
    media = round(media, 1)
    
    print(f"A media do aluno {numero_aluno}: {media}")

media_aluno(1)
media_aluno(2)
media_aluno(3)      