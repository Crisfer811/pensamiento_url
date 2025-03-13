#problema 1
consumo = float(input("Ingrese el consumo de agua en m³: "))
habitantes = int(input("Ingrese el número de habitantes: "))

if consumo < 15:
    tarifa = 5
elif 15 <= consumo <= 30:
    if habitantes > 3:
        tarifa = 4
    elif habitantes == 3:
        tarifa = 4.5
    else:
        tarifa = 5
else:  # consumo > 30
    if habitantes > 5:
        tarifa = 3.5
    elif habitantes % 2 == 0:
        tarifa = 4
    else:
        tarifa = 4.2

costo_total = consumo * tarifa
print("El costo total del consumo de agua es: Q",costo_total)




#problema 2
año_vehiculo = int(input("Ingrese el año del vehículo: "))
placa = input("Ingrese el número de placa del vehículo: ")
ultimo_digito = int(placa[-1])

if año_vehiculo >= 2001:
    if ultimo_digito in [0, 2, 4, 6, 8]:
        print("El vehículo NO circula los lunes.")
    else:
        print("El vehículo NO circula los viernes.")
    
    if año_vehiculo % 2 == 0:
        print("El vehículo solo circula hasta el mediodía los sábados.")

if 2024 - año_vehiculo > 25:
    print("Advertencia: El vehículo debe someterse a mantenimiento obligatorio.")
