def cuotaConAmortizacion(valorNominal, tasaEfectiva, numeroCupon, nCuotas, prima):
    print("---Cupon N(" + str(numeroCupon) + ") -----")
    tep = tasaEfectiva / 100
    #Cupon#
    print("\nCupon #" + str(numeroCupon) + " = TEP * Valor Nominal\nCupon #" + str(numeroCupon) + " = " + str(tasaEfectiva) + "% * " + str(valorNominal))
    cupon = tep * valorNominal
    cupon = round(cupon, 2)
    print("\nCupon #" + str(numeroCupon) + ": " + str(cupon))
    #Amortizacion#
    print("\nAmortizacion #" + str(numeroCupon) + " = Valor Nominal / (N - NC + 1)")
    amortizacion = valorNominal / (nCuotas - numeroCupon + 1)
    amortizacion = round(amortizacion, 2)
    print("\nAmortizacion #" + str(numeroCupon) + ": " + str(amortizacion))
    #Cuota#
    print("\nCuota #" + str(numeroCupon) + " = Cupon#" + str(numeroCupon) + " + Amortizacion" + str(numeroCupon))
    cuota = cupon + amortizacion
    cuota = round(cuota, 2)
    print("\nCuota #" + str(numeroCupon) + ": " + str(round(cuota, 2)))
    #Flujo
    if prima == 0.00:
        print("\n\nFlujo #" + str(numeroCupon) + " = Cuota #" + str(numeroCupon))
        print("\n\nFlujo #" + str(numeroCupon) + ": " + str(round(cuota, 2)))
    else:
        #Prima
        primaDelPeriodoFinal = prima * valorNominal #El valor nominal es al vencimiento del bono, es decir su valor en el ultimo cupon generado
        primaDelPeriodoFinal = round(primaDelPeriodoFinal, 2)
        print("\nPrima #" + str(numeroCupon) + " = %Prima * Valor Nominal")
        print("\nPrima #" + str(numeroCupon) + ": " + str(primaDelPeriodoFinal))
        #Flujo
        print("\n\nFlujo #" + str(numeroCupon) + " = Cuota #" + str(numeroCupon) + " + prima de vencimiento")
        print("\n\nFlujo #" + str(numeroCupon) + ": " + str(round(cuota + primaDelPeriodoFinal, 2)))

    #Nuevo Valor Nominal
    print("\nValor Nominal = Valor Nominal - Amortizacion #" + str(numeroCupon))
    valorNominal = valorNominal - amortizacion
    valorNominal = round(valorNominal, 2)
    print("\nValor Nominal: " + str(valorNominal))
    print("\n______________________________________________________________________\n")


######################################################################
def cuotaSinAmoritzacion(valorNominal, tasaEfectiva, numeroCupon):
    print("-----Cupon N(" + str(numeroCupon) + ")-----")
    #Cupon#
    print("\nCupon #" + str(numeroCupon) + " = TEP * Valor Nominal\nCupon #" + str(numeroCupon) + " = " + str(tasaEfectiva) + "% * " + str(valorNominal))
    cupon = (tasaEfectiva / 100) * valorNominal
    cupon = round(cupon, 2)
    print("\nCupon #" + str(numeroCupon) + ": " + str(cupon))
    #Amortizacion#
    print("\nAmortizacion #" + str(numeroCupon) + ": 0 (Por tratarse de periodo de gracia)")
    #Cuota#
    cuota = cupon
    cuota = round(cuota, 2)
    print("\nCuota #" + str(numeroCupon) + " = Cupon #" + str(numeroCupon) + " + 0.00")
    print("\nCuota #" + str(numeroCupon) + ": " + str(cuota))
    
    #Flujo
    print("\n\nFlujo #" + str(numeroCupon) + " = Cuota #" + str(numeroCupon))
    print("\n\nFlujo #" + str(numeroCupon) + ": " + str(cuota))
    #Nuevo Valor Nominal
    print("\nValor Nominal = Valor Nominal - Amortizacion #" + str(numeroCupon))
    print("\nValor Nominal = " + str(valorNominal) + " - 0.00\nValor Nominal = " + str(valorNominal))
    print("\n______________________________________________________________________\n")

##############################################################################################################################
    #Luego de sacar los resultados de cada cupón, de mencionarse alguna tasa descontada nueva
    #tener en cuenta esta formula: ejem(COK equivalente a tasa descontada 120 dias (d120)) de 1.0%
    #para hallar el COKp usamos el TEp = d120/(1-d120) --> TEp = 1.00% / (1 - 1.00%) --> TEp = 1.0101010%
    #finalmente ese TEp es igual al COKp que estamos hallando
    #Donde p es igual al periodo del cupon y calculado previamente en la formula (ejem: Trimestral, cuatrimestral, mensual, anual)
##############################################################################################################################
def precioValorFlujosDelCajaBono(flujosCajaBono, cok, nperiodos):
    local = 0.00
    precio = 0.00
    for x in range(nperiodos):
        local = float(input("Ingrese el flujo de caja " + str(x + 1) + ": "))
        flujosCajaBono.append(local)

    #Calculando la suma de flujos de caja
    for y in range(nperiodos):
        precio = precio + flujosCajaBono[y]/pow(1 + (cok/100), y + 1)
        precio = round(precio, 2)
    return precio

valorNominal = float(input("Ingrese el valor nominal: "))
tasaEfectiva = float(input("Ingrese la tasa efectiva: "))
nCuotas = int(input("Ingrese el numero de cuotas: "))
pregunta = " "
prima = 0.00
flujosCajaBono = []

for x in range(nCuotas):
    pregunta = input("¿Este Cupon#"+ str(x + 1)+ " tiene perdiodo plazo de gracia? (s: Si n: No): ")
    if pregunta == "s":
        cuotaSinAmoritzacion(valorNominal, tasaEfectiva, x + 1)
    else:
        valorNominal = float(input("Ingrese el ulitmo valor nominal recibido: "))
        pregunta = input("¿Incluye Prima este cupón (s: Si n: No): ")
        if pregunta == "s":
            prima = float(input("Ingrese la prima de vencimiento en (%): "))
            prima = prima / 100
            cuotaConAmortizacion(valorNominal, tasaEfectiva, x + 1, nCuotas, prima)
        else:
            cuotaConAmortizacion(valorNominal, tasaEfectiva, x + 1, nCuotas, prima)

cok = float(input("Ingrese la tasa de costo oportunidad: "))
precio = precioValorFlujosDelCajaBono(flujosCajaBono, cok, nCuotas)
print("Precio = " + str(precio))