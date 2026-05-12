"""
Tu tarea es escribir un programa en Python que haga lo siguiente:

1.  Solicite al usuario o usuaria los nombres de los clientes y clientas uno por uno y
    valide  que  cada nombre no esté vacío. Si se deja el campo vacío, mostrale un
    mensaje de advertencia y volvé a pedir el nombre.
2.  Guarde  cada  nombre  válido  en  una  lista,  asegurándote  de  agregarlo  con  el
    método .append().
3.  Permití que la persona finalice la carga de nombres escribiendo la palabra "fin".
4.  Una  vez  finalizada  la  carga,  ordená  alfabéticamente  los  nombres  en  la  lista  y
    mostrá la lista ordenada de nombres utilizando un bucle for.
"""

# ====================
# Creo una lista vacia
# ====================

nombres = []

# chamuyo
print(
    "Bienvenido al sistema de gestion de clientes:\n"
    'Para cargar un nuevo cliente ingrese su nombre, para finalizar la carga de datos escriba "fin" ',
)

# ========================================================
# utilizo un bucle WHILE para pedir y guardar los nombres
# ========================================================

while True:
    # limpio, formateo el dato y lo guardo en una variable
    nombre = input("Nombre: ").strip().title()

    # valido que nombre no esté vacío
    if nombre == "":
        print(
            "[ERROR]: el nombre no puede estar vacío, vuelva a ingresarlo correctamente..."
        )
        continue

    # si escribo "fin" salgo del bucle
    if nombre.lower() == "fin":
        print("Carga de datos finalizada")
        print("-------------------------")
        break

    # guardamos el nombre en la lista
    nombres.append(nombre)

    # debug
    # print(nombres)
    # salida esperada -> ['nombre1','nombre2','nombre3','nombreN']

# ===============================
# Ordeno la lista alfabeticamente
# ===============================
nombres.sort()

# =========================================================================
# Muestro lista de nombres ordenada alfabeticamente utilizando un bucle FOR
# =========================================================================

for nombre in nombres:
    print(f"-> {nombre}")
