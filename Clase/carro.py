anio= int(input(("Ingrese el año del carro: ")))
peso= int(input(("Ingrese el peso del carro: ")))


if anio < 2010:
    antiguedad="Antiguo"

    if peso < 1000:
        precio=300
    elif peso <= 1500:
        precio=400
    else:
        precio=500  

elif anio < 2020:
    antiguedad="Semi-nuevo"

    if peso < 1000:
        precio=400
    elif peso <= 1500:
        precio=550
    else:
        precio=700

else:
    antiguedad="Nuevo"

    if peso < 1000:
        precio=500
    elif peso <= 1500:
        precio=650
    else:
        precio=800

print(f'El carro es {antiguedad} y su precio es {precio}')