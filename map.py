# map
def dobro (x):
    return x*2

valor = [2, 3, 5, 6]

valor_dobrado  = map(dobro, valor)

valor_dobrado = list(valor_dobrado)
print (valor_dobrado)