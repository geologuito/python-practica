print("ingresar los datos a continuacion para avanzar:")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
correo = input("Correo electronico: ")

if edad >= 18:
    print("sos mayor de edad")
else:
    print("sos menor de edad")

if nombre == "" or apellido == "" or correo == "":
    print("ERROR!")

if nombre and apellido and correo:
    print("Datos ingresados correctamente")
