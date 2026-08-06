"""
Dado um ano, retorne o século em que está.
"""
def century(year):
    parte_inteira = year // 100 
    parte_decimal = year % 100

    if parte_decimal != 0:
        parte_inteira +=1

    return parte_inteira

print(century(2000)) 
print(century(1500)) 
    