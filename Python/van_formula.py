def Van_formula(inversion, flujoCaja, cok, periodo):
    local = 0.00
    van = 0.00
    for x in range(periodo):
        local = float(input("Ingrese el flujo de caja " + str(x + 1) + ": "))
        flujoCaja.append(local)

    #Calculando la suma de flujos de caja
    for y in range(periodo):
        van = van + flujoCaja[y]/pow(1 + (cok/100), y + 1)
    
    return van - inversion


inversion = float(input("Ingrese el monto de inversión: "))
flujoCaja = []
cok = float(input("Ingrese la tasa de costo de oportunidad(%): "))#ejem -> valor 2.012546%, ingresar 2.012546
periodo = int(input("Ingrese el número de periodos a calcular: "))

van = round(Van_formula(inversion, flujoCaja, cok, periodo), 2)

if van < 0.00:
    print("El resultado final del Van es menor a cero VAN->" + str(van) + ", por lo tanto no conviene")
elif van > 0.00:
    print("El resultado final del Van es mayor a cero VAN->" + str(van) + ", por lo tanto conviene")
else:
    print("El resultado final del Van es igual a cero VAN->" + str(van) + ", por lo tanto no importa")

#Para hallar el TIR usar calculadora cientifica
#En la constante TIR ingresar como x% <- incluya el porcentaje en la constante a hallar
#Finalmente el resultado le saldrá como si tuviese el porcentaje ya encontrado
#Ejem -> calculadora response -> 23.0217362 -> es como decir -> 23.0217362%