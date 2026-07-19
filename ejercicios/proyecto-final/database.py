import sqlite3


def inicializar_db():

    # conectando con la db
    conexion = sqlite3.connect("inventario.db")
    print("conección exitosa")

    # creamos un objeto cursor
    cursor = conexion.cursor()

    # creamos la tabla (si no existe)
    cursor.execute("""CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT
        )
    """)
    print("creamos la tablita")
    # confirmar cambios
    conexion.commit()

    # cerrar conexion
    conexion.close()
