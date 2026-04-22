"""
●   Solicite al cliente su nombre, apellido, edad y correo electrónico.
●   Almacene estos datos en variables.
●   Los muestre organizados en forma de una tarjeta de presentación en la pantalla.
❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗
❗      IMPORTANTE                                                ❗
❗  voy a usar f-strings:                                         ❗
❗      sintaxis => f"{valor:formato}"                            ❗
❗          valor => variable (nombre, edad, etc.)                ❗
❗          : => separa la variable del formato                   ❗
❗          formato => indica alineación, ancho, decimales, etc.  ❗
❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗

"""

# solicitamos los datos y los almacenamos:

nombre = input("ingrese su nombre:")  # nombre: => 8 caracteres
apellido = input("ingrese su apellido: ")  # apellido: => 10 caracteres
edad = input("ingrese su edad: ")  # edad: => 6 caracteres
correo = input("ingrese su correo electrónico: ")  # correo: => 8 caracteres

# mostramos la tarjeta superfachera de presentacion en la pantalla:

print("╔══════════════════════════════════════╗")  # son 40 caracteres
print("║                                      ║")
print(f"║{'TARJETA DE PRESENTACION':^38}║")
print("║                                      ║")
print(f"║ Nombre: {nombre:<29}║")
print(f"║ Apellido: {apellido:<27}║")
print(f"║ Edad: {edad:<31}║")
print(f"║ Correo: {correo:<29}║")
print("║                                      ║")
print("║                                      ║")
print("╚══════════════════════════════════════╝")
