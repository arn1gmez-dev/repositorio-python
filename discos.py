total_space= float(input("Escribe el espacio total del disco: "))
total_usage= float(input("Escribe el espacio ocupado: "))

def disk_space(total, disk):
    result= ""
    if total > disk:
        result= "Guardar el archivo"
    elif total == disk:
        result= "No se guarda el archivo"
    else:
        result= "ERROR"
    return result
print(disk_space(total_space, total_usage))