"""
Tu tarea es la siguiente:
    Parte 1:
    1.  Crear una lista con los nombres de los y las clientes que
        vamos a procesar.
    2.  Recorrer la lista con un for y mostrar el nombre de cada
        cliente junto con su posición en la lista (por ejemplo: Cliente
        1: Ana).
    3.  Si encuentras un nombre vacío, mostrar un mensaje de
    alerta indicando que ese dato no es válido.

    Ejemplo de salida:

    Cliente 1: Ana
    Cliente 2: Juan
    Cliente 3: [ALERTA] Nombre no válido
    Cliente 4: Marta

"""

# ==========================
# Inicializamos el contador
# ==========================
posicion = 0

# ==================
# Creamos la lista
# ==================

clientes = [
    "Ana",
    "Juan",
    "",
    "Marta",
    "Gonzalo",
    "Lucía",
    "Pedro",
]
# Recordatorio:
# Las listas empiezan en el índice 0
# clientes[0] -> "Ana"
# clientes[1] -> "Juan"
# clientes[2] -> ""

# =======================================
# Recorremos la lista en un bucle FOR
# =======================================
for cliente in clientes:
    # sumo 1 al contador al principio para que no le afecte el continue
    posicion += 1
    # si esta vacío muestro el Alert y la posicion
    if cliente.strip() == "":
        print(f"Cliente {posicion}: [ALERTA]: Nombre no valido")
        continue  # salteo el codigo que le sigue

    # Imprimo el nombre del cliente con su posicion
    print(f"Cliente {posicion}: {cliente}")
