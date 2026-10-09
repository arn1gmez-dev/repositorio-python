nota=float(input("Escribe tu nota: "))
if nota<0:
    print("Nota incorrecta")
elif nota <5:
    print("Insuficiente")
elif nota <6:
    print("Suficiente")
elif nota <7:
    print("Bien")
elif nota <9:
    print("Notable")
elif nota <=10:
    print("Sobresaliente")
else:
    print("Nota incorrecta")

print("Adiós")