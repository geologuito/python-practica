import sqlite3


import sqlite3


def inicializar_db():

    print("Inicializando base de datos...")

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    try:

        # Crea la tabla productos si todavía no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL,
                categoria TEXT
            )
        """)

        # Confirmamos los cambios realizados
        conexion.commit()

        print("Base de datos inicializada correctamente.")

    except sqlite3.Error as error:

        # Si ocurre un error, revertimos los cambios
        conexion.rollback()

        print(f"Error al inicializar la base de datos: {error}")

    finally:

        # Cerramos la conexión siempre
        conexion.close()
