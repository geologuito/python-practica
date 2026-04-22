"""

El programa debe:

- Pedir **nombre**, **apellido**, **edad** y **correo electrónico**
- Verificar que:
  - El nombre, apellido y correo **no estén vacíos**
  - La edad sea **mayor a 18**
- Si todo está bien, mostrar los datos
- Si **algo falla**, mostrar solamente: `"ERROR!"`

"""

print("Bienvenido al sistema de muestreo por favor ingrese sus datos:")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
correo = input("Correo electronico: ")
edad = int(input("Edad: "))


def verificar(nombre, apellido, correo, edad):
    if nombre.strip() and apellido.strip() and correo.strip() and edad > 18:
        print(f"Acceso concedido, bienvenido", nombre)
        return True
    else:
        print("Error de autenticacion")
        return False


if verificar(nombre, apellido, correo, edad):
    print("TODO pedimos las muestras")
else:
    print("no tenemos acceso")
