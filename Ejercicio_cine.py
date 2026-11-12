age = int(input("Introduce su edad:\n"))
student = input("Eres estudiante:\n")
day = input("¿Qué día es?:\n")


def precio_de_cine(age, day, student):
    precio = 8

    if day == "Miercoles" or day == "Miercoles":
        precio = 4
    elif age < 12:
        precio = 4
    elif age > 65:
        precio = 5
    elif student == "Si":
        precio = 5.6

    return precio


print("El precio de tu entrada es", precio_de_cine(age, day, student))