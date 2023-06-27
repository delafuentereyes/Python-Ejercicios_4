#Datos

import os
os.system("cls")

nombre = input("digite su nombre: ")
apellido = input("digite su apellido: ")
telefono = int(input("digite su telefono: "))
correo = input("digite su correo: ")
direccion = input("digite su direccion: ")

datos = {

    "nombre":nombre,
    "apellido":apellido,
    "telefono":telefono,
    "correo":correo,
    "direccion":direccion,
}

print (datos)