#Equipo

import os
os.system("cls")

diccionario = {}
lista = []


print("Digite la alineacion inicial de su equipo de futbol favorito")
print()

for i in range (11):

    numero = input ("Digite el numero del jugador: ")
    nombre = input("Digite el nombre del jugador: ")
    lista.append (numero)
    lista.append (nombre)

print (lista)
