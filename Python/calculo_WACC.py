impuestoRenta = 0.3

kd = float(input("Ingrese el Kd promedio: "))
d = float(input("Ingrese la suma de valores del denominador de kd (D): "))
ks = float(input("Ingrese el ks promedio: "))
s = float(input("Ingrese la suma de valores del denominador de ks (S): "))

wacc = kd / 100 * (d / (d + s)) * (1-impuestoRenta) + ks / 100 * (s / (d + s))

print("WACC = " + str(round(wacc*100, 7)) + "%")