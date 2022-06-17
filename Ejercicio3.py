
nombre = input("Ingrese su nombre: ")
apellidos = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
dni = input("Ingrese su DNI: ")

Dicc1 = {"Nombre": nombre, "Apellidos": apellidos, "Edad": edad, "DNI": dni}
lista1 = list(Dicc1)
print("El tipo de dato de la lista1 es: ", type(lista1))
print("El diccionario actual es: ", Dicc1)

Dicc1["Profesión"] = "Ing. Industrial"
del Dicc1["DNI"]

print("El diccionario final es: ", Dicc1)