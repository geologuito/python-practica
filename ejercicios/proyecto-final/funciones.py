from colorama import Fore, Style
import sqlite3


# Muestra las opciones disponibles del sistema
def mostrar_menu():
    print("""
==============================
Sistema de Gestión de Inventario
==============================

1. Registrar producto
2. Mostrar productos
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Reporte de stock bajo
7. Salir
""")


# Funciones auxiliares para validar entradas numéricas del usuario
# Solicita un valor entero al usuario y valida que la entrada sea correcta
def pedir_entero(mensaje):

    while True:
        try:
            valor = int(input(mensaje))
            return valor

        except ValueError:
            print("Ingrese un número entero válido.")


# Solicita un valor decimal al usuario y valida que la entrada sea correcta
def pedir_float(mensaje):

    while True:
        try:
            valor = float(input(mensaje))
            return valor

        except ValueError:
            print("Ingrese un número válido.")


# Solicita los datos del producto y devuelve la información ingresada
def pedir_datos_producto():

    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    cantidad = pedir_entero("Cantidad: ")
    precio = pedir_float("Precio: ")
    categoria = input("Categoría: ")

    return nombre, descripcion, cantidad, precio, categoria


# llama a la funcion anterior y registra los datos en la base de datos
def registrar_producto():
    nombre, descripcion, cantidad, precio, categoria = pedir_datos_producto()

    # conectamos a la base de datos
    conexion = sqlite3.connect("inventario.db")
    # creamos un objeto cursor
    cursor = conexion.cursor()

    try:
        # Insertamos el producto
        cursor.execute(
            """
            INSERT INTO productos
            (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        """,
            (nombre, descripcion, cantidad, precio, categoria),
        )

        # Confirmamos los cambios
        conexion.commit()

        print(Fore.GREEN + "Producto registrado correctamente." + Style.RESET_ALL)

    except sqlite3.Error as error:

        # Si hay un error, deshacemos los cambios
        conexion.rollback()

        print(Fore.RED + f"Error al registrar el producto: {error}" + Style.RESET_ALL)

    finally:

        # Cerramos la conexión
        conexion.close()


def mostrar_todos_productos():

    # Abrimos la conexión con la base de datos
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    try:
        # Obtiene todos los productos registrados
        cursor.execute("SELECT * FROM productos")

        productos = cursor.fetchall()

        # Validamos si existen productos
        if not productos:
            print("No hay productos registrados.")
            return

        # Recorremos la lista de productos
        for producto in productos:

            id_producto = producto[0]
            nombre = producto[1]
            descripcion = producto[2]
            cantidad = producto[3]
            precio = producto[4]
            categoria = producto[5]

            print(f"""
            ID: {id_producto}
            Nombre: {nombre}
            Descripcion: {descripcion}
            Cantidad: {cantidad}
            Precio: {precio}
            Categoria: {categoria}
            """)

    except sqlite3.Error as error:

        print(f"Error al mostrar productos: {error}")

    finally:

        # Cerramos la conexión
        conexion.close()


def buscar_producto():

    id_buscar = pedir_entero("Ingrese ID del producto: ")

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_buscar,))

        producto = cursor.fetchone()

        if producto:
            # variables
            id_producto = producto[0]
            nombre = producto[1]
            descripcion = producto[2]
            cantidad = producto[3]
            precio = producto[4]
            categoria = producto[5]
            print(f"""
            ID: {id_producto}
            Nombre: {nombre}
            Descripcion: {descripcion}
            Cantidad: {cantidad}
            Precio: {precio}
            Categoria: {categoria}
            """)
        else:
            print("Producto no encontrado.")

    except sqlite3.Error as error:
        print(f"Error al buscar producto: {error}")

    finally:
        conexion.close()


def actualizar_producto():

    # Pedimos el ID del producto a modificar
    id_producto = pedir_entero("Ingrese el ID del producto a actualizar: ")

    # Pedimos los nuevos datos
    nombre, descripcion, cantidad, precio, categoria = pedir_datos_producto()

    # Conectamos a la base de datos
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    try:

        cursor.execute(
            """
            UPDATE productos
            SET nombre = ?,
                descripcion = ?,
                cantidad = ?,
                precio = ?,
                categoria = ?
            WHERE id = ?
        """,
            (nombre, descripcion, cantidad, precio, categoria, id_producto),
        )

        # verificamos si se modificó algún registro
        if cursor.rowcount > 0:

            conexion.commit()
            print("Producto actualizado correctamente.")

        else:

            print("No existe un producto con ese ID.")

    except sqlite3.Error as error:

        conexion.rollback()
        print(f"Error al actualizar producto: {error}")

    finally:

        conexion.close()


def eliminar_producto():

    id_producto = pedir_entero("Ingrese el ID del producto a eliminar: ")
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    try:

        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))

        if cursor.rowcount > 0:

            conexion.commit()
            print("Producto eliminado correctamente.")

        else:

            print("No existe un producto con ese ID.")

    except sqlite3.Error as error:

        conexion.rollback()
        print(f"Error al eliminar producto: {error}")

    finally:

        conexion.close()


def reporte_stock_bajo():

    limite = pedir_entero("Ingrese el límite de stock: ")

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    try:

        cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))

        productos = cursor.fetchall()

        if productos:

            for producto in productos:

                id_producto = producto[0]
                nombre = producto[1]
                descripcion = producto[2]
                cantidad = producto[3]
                precio = producto[4]
                categoria = producto[5]

                print(f"""
                ID: {id_producto}
                Nombre: {nombre}
                Descripción: {descripcion}
                Cantidad: {cantidad}
                Precio: {precio}
                Categoría: {categoria}
                """)

        else:
            print("No hay productos con stock bajo.")

    except sqlite3.Error as error:

        print(f"Error al generar reporte: {error}")

    finally:

        conexion.close()
