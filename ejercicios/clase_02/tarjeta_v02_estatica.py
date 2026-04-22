"""
📌 Uso de f-strings en este archivo

Se utilizan f-strings para alinear y formatear el texto dentro de la tarjeta.

🔹 Sintaxis:
    f"{valor:formato}"
🔹 Componentes:
    - valor: variable o expresión (nombre, edad, etc.)
    - :     separa el valor del formato
    - formato: define alineación, ancho, etc.
🔹 Ejemplos usados:
    {texto:<n}  → alinear a la izquierda
    {texto:^n}  → centrar texto

🔗 Recursos:
https://www.w3schools.com/python/python_strings_format.asp
https://www.w3schools.com/python/python_string_formatting.asp
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
