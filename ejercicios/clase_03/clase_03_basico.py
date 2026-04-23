"""
Desarrollar un programa que:

- Solicite nombre, apellido, edad y correo electrónico
- Verifique que:
    - nombre, apellido y correo no estén vacíos
    - edad sea mayor a 18
- Si todo está bien, mostrar los datos
- Si algo falla, mostrar "ERROR!"
"""

# =========================
#   Entrada de datos
# =========================
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
correo = input("Correo electrónico: ")

# =========================
#   Validacion de datos
# =========================
if nombre != "" and apellido != "" and correo != "" and edad > 18:
    print("Nombre:             " + nombre)
    print("Apellido:           " + apellido)
    print("Edad:               " + str(edad))
    print("Correo electrónico: " + correo)
else:
    print("ERROR!")