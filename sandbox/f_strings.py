"""
🎮 Nivel 1 — Básico

👉 Mostrá este mensaje usando f-string:

Hola Gonzalo

Pero:

Usá una variable nombre

Usá f-string (no concatenación)
"""

nombre = "Gonzalo"

print(f"Hola {nombre}")

################################################

"""
🎮 Nivel 2 — Expresión

👉 Mostrá:

El próximo año tendrás 35 años

Condiciones:

Tenés edad = 34

Hacé el cálculo dentro del f-string 
"""

edad = 34
print(f"El proximo año tendrás {edad+1} años")

################################################

"""
🎮 Nivel 3 — Alineación

👉 Mostrá la palabra:

Python

Centrada en 20 caracteres
"""

print(f"{'Python':^20}")

################################################

"""
🎮 Nivel 4 — Relleno fachero 😏

👉 Mostrá:

****Python****

Pero:

Usando f-string

Sin escribir los * a mano (tienen que salir del formato)
"""

print(f"{'Python':*^14}")

################################################

"""
🎮 Nivel 5 — Debug GOD 🔥

Dadas estas variables:

x = 10
y = 5

👉 Mostrá exactamente:

x=10, y=5, suma=15
"""

x = 10
y = 5

print(f"{x=}, {y=}, suma={x+y}")
