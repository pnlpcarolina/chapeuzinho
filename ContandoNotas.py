# -*- coding: utf-8 -*-

### Este é um contador da média de notas de um estudante, o programa deve mostrar a média e aprovação/reprovação após a inserção das duas notas.
    

def prova1():
    n=float(input('Digite a nota da 1ª prova: '))
    return n

def prova2():
    n=float(input('Digite a nota da 2ª prova: '))
    return n 

def resultado(n1,n2):
    media=(n1+n2)/2
    print("Nota 1: ",n1)
    print("Nota 2: ",n2)
    print("Média: ", media, "\nResultado: ", end="")
    if media >=7:
        print("Aprovado")
    else:
        print("Reprovado")
    
a = prova1()
b = prova2()
resultado(a,b)