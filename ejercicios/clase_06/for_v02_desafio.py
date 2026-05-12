"""
# Desafío - Limpiar y mostrar una lista de nombres

Tenemos una lista con nombres de personas que se anotaron a una capacitación.
Pero algunos tienen problemas:

- Algunos están **vacíos o con espacios solamente**
- Otros tienen **mayúsculas y minúsculas mal combinadas**

Tu tarea es:

1. Recorrer la lista con un `for`
2. Ignorar los valores vacíos o incorrectos usando `continue`
3. Mostrar solo los nombres válidos, **bien formateados** (con `.strip()` y `.title()`)

🔧 Bonus: al final, mostrar cuántos nombres válidos se encontraron.
"""

# ============================
# Inicializamos contador
# ============================
cantidad_validos = 0

# ==================
# Creamos la lista
# ==================
nombres = [
    "ana",
    "   juan",
    "",
    "mARta",
    "   ",
    "gOnZaLo",
    "LUCÍA",
    "pedro   ",
    "  maRIA de los angeles  ",
    "\t",
    "cArLoS",
    "sofia",
    "   eMILIANO",
    "VALENTINA   ",
]
# Guardo la cantidad de datos que vienen en la lista
total_nombres = len(nombres)

print("===============================================")
print("Lista de personas anotadas a la capacitacion: ")
print("===============================================")

# =======================================
# Recorremos la lista en un bucle FOR
# =======================================
for nombre in nombres:
    # DEBUG
    # print(f"antes del format: {nombre}")
    # salida esperada -> antes del format: mARta

    # Limpio y formateo el dato
    nombre = nombre.strip().title()

    # si el dato viene vacío, lo ignoro
    if nombre == "":
        # DEBUG
        # print(f"dentro del if: {nombre}")
        # salida esperada -> dentro del if _(espacio en blanco)
        continue  # salteo el codigo que le sigue

    # aumento el contador en 1 unidad
    cantidad_validos += 1

    # Imprimo nombre correctamente formateado y ordenado numericamente
    print(f"Alumno {cantidad_validos}: {nombre}")

print("===============================================")
print(f"La cantidad de nombres validos es: {cantidad_validos} de {total_nombres}")
print("===============================================")
