#Super

import os
os.system("cls")

lista = []
diccionario = {}


canti_productos = int(input("Digite la cantidad de productos que desea revisar: "))

for i in range (canti_productos):

    producto = input("digite el producto: ")
    cant_unidad = input("digite la cantidad de existencias: ")

    productos = [producto, cant_unidad]
    lista.append (productos)

print (lista)
    
