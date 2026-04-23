"""
Resolución de la guía de f-strings
Ver: guias/guia_fstrings.md
"""

# Nivel 1: Basico
nombre = "Gonzalo"
print(f"Hola {nombre}")

# Nivel 2: Expresión
edad = 34
print(f"El proximo año tendrás {edad+1} años")

# Nivel 3: Alineación
print(f"{'Python':^20}")

# Nivel 4: Relleno
print(f"{'Python':*^14}")

# Nivel 5: Debug
x = 10
y = 5
print(f"{x=}, {y=}, suma={x+y}")