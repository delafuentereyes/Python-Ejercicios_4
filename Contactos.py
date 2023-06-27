#Contactos

import os
os.system("cls")

canti_contactos = int(input("¿Cuantos contactos desea ingresar? "))

for i in range (canti_contactos):

    nombre = input("Digite el nombre del nuevo contacto: ")
    numero = int(input("Digite el numero telefonico del nuevo contacto: "))

agenda = {

    "nombre":nombre,
    "numero":numero,
}

print(agenda)