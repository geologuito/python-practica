"""
Desarrollar un programa que:
●   Solicite al cliente su nombre, apellido, edad y correo electrónico.
●   Almacene estos datos en variables.
●   Los muestre organizados en forma de una tarjeta de presentación en la pantalla.
"""
# =========================
#   Entrada de datos
# =========================
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
correo = input("Correo electrónico: ")


# =========================
#   Tarjeta de presentación
# =========================

print("---------------------------------------------------")
print("              TARJETA DE PRESENTACIÓN              ")
print("---------------------------------------------------")
print(" Nombre:             " + nombre)
print(" Apellido:           " + apellido)
print(" Edad:               " + edad)
print(" Correo electrónico: " + correo)
print("---------------------------------------------------")