"""aca va el docstring"""

# datos
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
correo = input("Ingrese su correo electrónico: ")

# contenido (lo armamos como texto primero)
lineas = [
    "TARJETA DE PRESENTACION",
    "",
    f"Nombre: {nombre}",
    f"Apellido: {apellido}",
    f"Edad: {edad}",
    f"Correo: {correo}",
    "",
]


# max(len(linea) for linea in lineas)
# recorre cada línea, calcula su longitud
# y devuelve la longitud máxima
ancho = max(len(linea) for linea in lineas)

# dibujamos la tarjeta
print("╔" + "═" * (ancho + 2) + "╗")

for linea in lineas:

    print(f"║ {linea:<{ancho}} ║")

print("╚" + "═" * (ancho + 2) + "╝")
