############(B/C) --> Beneficio/Costo
def benAndCosto(inversion, periodo, cok, flujoCaja):
    bc = 0.0
    for x in range(periodo):
        bc = float(input("Ingrese el flujo de caja " + str(x + 1) + ": "))
        flujoCaja.append(bc)
    bc = 0.0

    for y in range(periodo):
        bc = bc + flujoCaja[y]/pow(1 + (cok/100), y + 1)
    
    return bc / inversion

inversion = float(input("Ingrese el monto de inversión: "))
flujoCaja = []
cok = float(input("Ingrese la tasa de costo de oportunidad(%): "))
periodo = int(input("Ingrese el número de periodos a calcular: "))

bc = round(benAndCosto(inversion, periodo, cok, flujoCaja), 7)

if bc < 0.00:
    print("El resultado final del (Beneficio/Costo) es menor a cero B/C->" + str(bc) + ", por lo tanto no conviene")
elif bc > 0.00:
    print("El resultado final del (Beneficio/Costo) es mayor a cero B/C->" + str(bc) + ", por lo tanto conviene")
else:
    print("El resultado final del (Beneficio/Costo) es igual a cero B/C->" + str(bc) + ", por lo tanto no importa")