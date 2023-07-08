################### Calculo de PRD ######################
def PRD_FUNCTION(X1, Y1, X2, Y2):
    print("\n\nCoordenada P1 es (" + str(X1) + ", " + str(Y1) + ")\n")
    print("\nCoordenada P2 es (" + str(X2) + ", " + str(Y2) + ")\n")
    #Calculamos la pendiente de la recta | Fórmula -> m = (y2 - y1) / (x2 - x1)
    m = 0.0
    pdr = 0.0
    m = (Y2 - Y1) / (X2 - X1)

    #Luego hallamos el PDR final | punto 3 (P3): (X3, Y3) --> (PDR, 0)
    #Entonces la ecuación sería m (hallado previamente) --> (Y3 - Y2) / (X3 - X2) = m
    #Despejando variables para hallar el PDR, quedaría --> ((Y3 - Y2) / m) + X2 = PDR
    pdr = ((0 - Y2) / m) + X2 

    return pdr

################## Hallar VAN ############################
def VAN_FIRST_PAST(inversion, cok, periodo, flujoCaja):
    local = 0.00
    van = -inversion
    for x in range(periodo):
        local = float(input("Ingrese el flujo de caja " + str(x + 1) + ": "))
        flujoCaja.append(local)

    print("VAN en (t = 0): " + str(van) + " <- Inversion / Flujo Siguiente -> " + str(round(flujoCaja[0]/pow(1 + (cok/100), 1), 2)))
    van = van + flujoCaja[0]/pow(1 + (cok/100), 1)
    #Calculando la suma de flujos de caja
    for y in range(periodo + 1):
        if y + 1 < len(flujoCaja):
            print("VAN en (t = " + str(y + 1) + "): " + str(van) + " <- Inversion / Flujo Siguiente -> " + str(round(flujoCaja[y + 1]/pow(1 + (cok/100), y + 2), 2)))
            van = van + flujoCaja[y + 1]/pow(1 + (cok/100), y + 2)
        else:
            print("VAN en (t = " + str(y + 1) + "): " + str(van))
            break
        
    return van

inversion = float(input("Ingrese el monto de inversión: "))
flujoCaja = []
cok = float(input("Ingrese la tasa de costo de oportunidad(%): "))
periodo = int(input("Ingrese el número de periodos a calcular: "))
prd = 0.00
van = round(VAN_FIRST_PAST(inversion, cok, periodo, flujoCaja), 2)
if van < 0.00:
    print("El resultado final del Van es menor a cero VAN->" + str(van) + ", por lo tanto no conviene\n\n")
elif van > 0.00:
    print("El resultado final del Van es mayor a cero VAN->" + str(van) + ", por lo tanto conviene\n\n")
    print("Hallando el PRD, Segun los valores obtenidos en la operacion del VAN\nDonde (X1, Y1) son cordenadas del periodo y VAN negativo antes del siguiente positivo\nY (X2, Y2) son coordenadas del periodo y VAN cuyo signo cambie\n\n")
    x1=float(input("\tIngrese X1: "))
    y1=float(input("\tIngrese Y1: "))
    x2=float(input("\tIngrese X2: "))
    y2=float(input("\tIngrese Y2: "))
    prd = PRD_FUNCTION(x1, y1, x2, y2)
    print("EL PRD es: " + str(prd) + " años") #2.512313
    anios = int(prd) 
    meses = (prd - anios) * 12 #(2.512313 - 2)*12 =  (0.512313 * 12) = 6.147756
    meses = int(meses)
    dias = round((((prd - anios) * 12) - meses) * 30)
    print(str(anios) + "años " + str(meses) + "meses " + str(dias) + "dias :)")
else:
    print("El resultado final del Van es igual a cero VAN->" + str(van) + ", por lo tanto no importa\n\n")