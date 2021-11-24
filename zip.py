# zip

lista1 = [1,2,3,4]
lista2 = ["bola", "abacate", "elefante", "dinheiro"]
lista3 = ["R$2,00", "R$3,00", "Não tem preço", "Não tem preço"]

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)