"""
Necesitamos  que  tu  programa  cumpla  con  estas
instrucciones:
●  Crear un diccionario llamado productos donde las claves sean los nombres
de los productos y los valores sean sus precios.
●  Permitir agregar productos y sus precios hasta que se decida finalizar.
●  Mostrar el contenido del diccionario después de cada operación.
"""

# ====================
# definimos variables
# ====================
productos = {}
continuar = True

# loop para cargar productos
while continuar:
    # carga y limpieza de datos
    producto = input("Producto: ").strip().lower()
    precio = input("Precio: ").strip()

    # validacion de campos vacios
    if producto == "" or precio == "":
        print(
            "[ERROR]: Los campos no pueden estar vacios vuelva a ingresar el producto.."
        )
        continue

    # valido que precio sea un numero (por ahora entero)
    if not precio.isdigit():
        print("[ERROR]: el precio debe ser un numero")
        continue

    # guardado de datos
    productos[producto] = int(precio)

    # visualizacion de datos
    for producto, precio in productos.items():
        print(f">> {producto:<10}: {'$':>5}{precio:.2f}")
    print("----------------------------------------------")
    # ==============================
    # validar respuesta si/no
    # ==============================
    while True:
        if_continuar = input("desea agregar un nuevo producto? si/no: ").strip().lower()
        if if_continuar == "si":
            break
        if if_continuar == "no":
            print("carga de productos finalizada")
            continuar = False
            break
        print("[ERROR]: ingrese solamente 'si' o 'no'")
