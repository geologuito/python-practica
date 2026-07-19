import database
import funciones

# inicializamos la base de datos
database.inicializar_db()

# declaracion de variables globales
salir = False

# menu principal
while not salir:
    funciones.mostrar_menu()

    opcion = input("Elija un opción: ")
    print("")
    match opcion:
        case "1":
            funciones.registrar_producto()
        case "2":
            funciones.mostrar_todos_productos()
        case "3":
            funciones.buscar_producto()
        case "4":
            funciones.actualizar_producto()
        case "5":
            funciones.eliminar_producto()
        case "6":
            funciones.reporte_stock_bajo()
        case "7":
            print("Salir")
            salir = True
        case _:
            print("Opcion Invalida")
