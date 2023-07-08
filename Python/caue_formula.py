def caueFormula(vac, ti, p):
    a = ti * pow(1+ti, p)
    b = pow(1 + ti, p) - 1
    return vac * a/b


###################################################################
vac = input("Inserta vac: ")
vac = float(vac)

i = input("Inserta tasa (%): ")
i = float(i)
i = i/100
p = input("Inserta plazo de baja/tiempo vida util: ")
p = int(p)

print("CAUE: ", round(caueFormula(vac, i, p), 2))