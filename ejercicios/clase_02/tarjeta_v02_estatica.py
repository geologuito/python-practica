"""
Uso de f-strings para formatear la tarjeta.

📌 Ver guía completa:
guias/guia_fstrings.md
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

# Línea superior del recuadro
print("╔══════════════════════════════════════╗")

# Línea vacía
print("║                                      ║")

# Título centrado
print(f"║{'TARJETA DE PRESENTACION':^38}║")

# Línea vacía
print("║                                      ║")

# Datos alineados a la izquierda con ancho fijo
print(f"║ Nombre: {nombre:<29}║")
print(f"║ Apellido: {apellido:<27}║")
print(f"║ Edad: {edad:<31}║")
print(f"║ Correo: {correo:<29}║")

# Líneas vacías finales
print("║                                      ║")
print("║                                      ║")

# Línea inferior del recuadro
print("╚══════════════════════════════════════╝")
