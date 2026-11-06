edad=int(input("Ingrese su edad: "))
Estudiante = input("¿Eres estudiante?: ")
dia=input("Ingrese el dia: ")
precio_base= 8
if edad < 12:
    precio_menores= precio_base/2
    print("Paga la mitad", precio_menores)
elif dia == "miércoles":
    print("pagas 4")
elif Estudiante == "si":
    precio_estudiante= precio_base*0.3
    print("Paga el descuento de estudiante", precio_base - precio_estudiante)
elif edad > 65 :
    print("Precio reducido: 5")
