"""
Simulador de muestreo geológico (sandbox)

Este script es una versión experimental donde:
- se prueban validaciones
- uso de funciones
- lógica de flujo

No corresponde a una clase específica del curso.
"""
print("Bienvenido al sistema de muestreo por favor ingrese sus datos:")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
correo = input("Correo electronico: ")
edad = int(input("Edad: "))


def verificar(nombre, apellido, correo, edad):
    if nombre.strip() and apellido.strip() and correo.strip() and edad > 18:
        print(f"Acceso concedido, bienvenido", nombre)
        return True
    else:
        print("Error de autenticacion")
        return False


if verificar(nombre, apellido, correo, edad):
    print("TODO pedimos las muestras")
else:
    print("no tenemos acceso")
