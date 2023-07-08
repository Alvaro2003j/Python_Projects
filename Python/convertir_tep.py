def tep_to_tep(tasaQueTengo, periodoDeTasaQueTengo, periodoDeTasaQueQuiero):
    tasaQueQuiero = pow(1+tasaQueTengo, periodoDeTasaQueQuiero/periodoDeTasaQueTengo) - 1
    return tasaQueQuiero

tasaQueTengo = float(input("Tasa que tengo (%): "))
tasaQueTengo = tasaQueTengo / 100

periodoDeTasaQueTengo = int(input("Periodo de tasa que tengo: "))

periodoDeTasaQueQuiero = int(input("Periodo de tasa que quiero: "))

print("La tasa de efectiva que quiero es: " + str(round(tep_to_tep(tasaQueTengo, periodoDeTasaQueTengo, periodoDeTasaQueQuiero) * 100, 7)) + "%")

