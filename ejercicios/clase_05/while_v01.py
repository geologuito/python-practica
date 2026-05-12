"""
Te propongo que uses y combines varias herramientas que hemos visto:

🔹 `while` para repetir acciones
🔹 Validación de datos (no se aceptan ingresos negativos)
🔹 Acumulación de valores
🔹 Mostrar un resumen final con el total de ingresos


Para escribir un programa que:

1. Con un bucle `while` le pida los ingresos mensuales de los últimos **6 meses**
2. Si el valor ingresado es negativo, mostrá un mensaje y volvé a pedir el dato
3. Sumá todos los ingresos válidos
4. Al final, mostrale al usuario su **total acumulado en 6 meses** y su promedio.

💡 Consejo: podés usar una lista para guardar los ingresos si querés, aunque no es obligatorio.
"""

# Variables
mes = 1
suma = 0

while mes <= 6:
    # esto es mejorable porque se puede romper si esta vacio o si ingreso letras
    ingreso = int(input(f"ingreso del mes {mes}: "))

    if ingreso < 0:
        print(f"Error: Formato invalido")
        # debug
        # print(f"Ingreso: {ingreso}")
        # print(f"Suma:{suma}")
        continue

    suma += ingreso
    # debug
    # print(f"Suma: {suma}")
    mes += 1

promedio = suma / 6
print("Resumen:")
print("-----------------------------")
print(f"Total acumulado en 6 meses: ${suma}")
print(f"Promedio: ${promedio:.2f}")
print("-----------------------------")
