"""Sistema de Gestion de Productos"""

# declaracion de variables

productos = [
    {"nombre": "manzana", "categoria": "fruta", "precio": 100},
    {"nombre": "banana", "categoria": "fruta", "precio": 200},
    {"nombre": "leche", "categoria": "lacteos", "precio": 300},
]

# debug
while True:

    print("""
=============================
    Gestion de Productos
=============================

1. Agregar producto
2. Mostrar productos
3. Buscar producto
4. Eliminar producto
5. Salir
""")

    opcion = input("seleccione una opcion: ")
    print("--------------------")
    match opcion:
        # ==================
        # agregar producto
        # ==================
        case "1":
            while True:
                nombre = input("Nombre: ").strip().lower()
                categoria = input("Categoria: ").strip().lower()
                precio = input("Precio: ").strip()

                if nombre == "" or categoria == "" or precio == "":
                    print("[ERROR] No puede haber campos vacíos")
                    continue

                if not precio.isdigit():
                    print("[ERROR] El precio debe ser un número entero")
                    continue

                producto = {
                    "nombre": nombre,
                    "categoria": categoria,
                    "precio": int(precio),
                }

                productos.append(producto)
                print("Producto agregado")
                break

        # ==================
        # mostrar productos
        # ==================
        case "2":
            posicion = 1
            for producto in productos:
                print(
                    f"{posicion}. {producto['nombre']} - {producto['categoria']} - ${producto['precio']}"
                )
                posicion += 1

        # ==================
        # buscar por nombre
        # ==================
        case "3":
            buscado = input("Buscar producto: ").strip().lower()

            encontrado = False

            for producto in productos:
                if producto["nombre"] == buscado:
                    print(
                        f"{producto['nombre']} - {producto['categoria']} - ${producto['precio']}"
                    )
                    encontrado = True

            if not encontrado:
                print("No se encontraron resultados")

        # ==================
        # eliminar producto
        # ==================
        case "4":
            indice = input("Ingrese número a eliminar: ").strip()

            if not indice.isdigit():
                print("[ERROR] Debe ingresar un número")
                continue

            indice = int(indice)

            if indice < 1 or indice > len(productos):
                print("[ERROR] Índice fuera de rango")
                continue

            eliminado = productos.pop(indice - 1)
            print(f"Eliminado: {eliminado['nombre']}")

        # ==================
        # salir
        # ==================
        case "5":
            print("Saliendo del sistema...")
            break

        # ==================
        # otro
        # ==================
        case _:
            print("[ERROR]: Opcion invalida")
    print("--------------------")
