def fuctionVAC(pv, r, i, p, s):
    vac = pv - round(s/pow(1+i, p), 2)
    for x in range(p):
        vac = vac + (round(r/pow(1 + i, x + 1), 2))
    return vac


pv = input("Inserta Pv: ")
r = input("Inserta todos los gastos/costos existentes: ")
i = input("Inserta tasa (%): ")
p = input("Inserta el plazo de baja: ")
s = input("Inserta Salvataje del equipo: ")

pv = float(pv)
r = float(r)
i = float(i)
i = i/100
p = int(p)
s = float(s)


print("VAC: ", round(fuctionVAC(pv, r, i, p, s), 2))
#def fuctionVAC(pv, gastosAnuales, tasa, nperiodo, salvataje):
#    vac = 0.00
#    vac = pv + gastosAnuales * (pow(1+tasa, nperiodo) - 1) / (tasa * pow(1 + tasa, nperiodo))
#    return vac - (salvataje / pow(1+tasa, 7))
#
#pv = input("Inserta Pv: ")
#r = input("Inserta gastos anuales totales: ")
#i = input("Inserta tasa (%): ")
#p = input("Inserta # periodo: ")
#s = input("Inserta Salvataje: ")
#
#pv = float(pv)
#r = float(r)
#i = float(i)
#i = i/100
#p = int(p)
#s = float(s)
#
#print("VAC: ", round(fuctionVAC(pv, r, i, p, s), 2))