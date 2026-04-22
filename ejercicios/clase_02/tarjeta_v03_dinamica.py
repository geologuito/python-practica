# =========================
#   Entrada de datos
# =========================
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
correo = input("Correo electrónico: ")

# =========================
#   Armamos el contenido
# =========================
# Guardamos cada línea de la tarjeta en una lista
lineas = [
    "TARJETA DE PRESENTACION",
    "",
    f"Nombre: {nombre}",
    f"Apellido: {apellido}",
    f"Edad: {edad}",
    f"Correo: {correo}",
    "",
]

# =========================
#   Calculamos el ancho
# =========================
# Buscamos la línea más larga para ajustar el tamaño de la tarjeta
ancho = max(len(linea) for linea in lineas)

# =========================
#   Dibujamos la tarjeta
# =========================

print("╔" + "═" * (ancho + 2) + "╗")
# Recorremos cada línea y la mostramos alineada dentro del recuadro
for linea in lineas:
    print(f"║ {linea:<{ancho}} ║")

print("╚" + "═" * (ancho + 2) + "╝")
