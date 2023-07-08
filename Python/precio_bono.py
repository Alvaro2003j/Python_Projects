def flujoTotal(numeroPeriodos, flujo, Coks):
    flujoResultado = 0.0
    parcial = 0.0
    for i in range(numeroPeriodos):
        parcial = input("Flujo #" + str(i + 1) + ": ")
        parcial = float(parcial)
        flujo.append(parcial)

    for j in range(numeroPeriodos):
        flujoResultado = flujoResultado + flujo[j]/pow((1+Coks/100), j+1)
        print(round(flujo[j]/pow((1+Coks/100), j+1), 2))

    return flujoResultado


numeroPeriodos = input("Numero de Periodos: ")
numeroPeriodos = int(numeroPeriodos)

flujo = []

coks = input("COKs: ")
coks = float(coks)

respueta = flujoTotal(numeroPeriodos, flujo, coks)
respueta = round(respueta, 2)
print("El Precio del bono es: " + str(respueta))