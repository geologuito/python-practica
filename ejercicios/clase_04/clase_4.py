"""
Nuestro cliente nos pide que el programa que has desarrollado ahora haga lo siguiente:

Formatee correctamente los textos ingresados en “apellido” y “nombre”, convirtiendo la primera letra de cada palabra a mayúsculas y el resto en minúsculas.

Asegurarse que el correo electrónico no tenga espacios y contenga solo una “@”.

Que clasifique por rango etario basándose en su edad (“Niño/a” para los menores de 15 años, “Adolescente” de 15 a 18 y “Adulto/a” para los mayores de 18 años.)
"""
# ==================================================
#   Entrada de datos + definicion de variables
# ==================================================
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
correo = input("Correo electronico: ")
rango_etario = "" #esto no es necesario yo lo puse por costumbre.


# =========================
# VALIDAMOS LOS DATOS
# =========================
# - campos no vacíos
# - solo 1 arroba en el correo
if not nombre.strip() or not apellido.strip() or not correo.strip() or correo.count("@") != 1 or correo.count(" ")!= 0:
    print("ERROR!")
    
else:
    # =========================
    # PROCESAMOS LA INFORMACIÓN
    # =========================
    # clasificamos según edad
    if edad > 18:
        rango_etario = "Adulto/a"
    elif edad >= 15:
        rango_etario = "Adolescente"
    else:
        rango_etario = "Niño/a"
        
    # =========================
    # MOSTRAMOS RESULTADOS
    # =========================
    print(f"Nombre:             {nombre.title()}")
    print(f"Apellido:           {apellido.title()}")
    print(f"Edad:               {edad}")
    print(f"Correo electrónico: {correo}")
    print(f"Rango etario:       {rango_etario}")
