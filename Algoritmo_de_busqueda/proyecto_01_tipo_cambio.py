#proyecto_01_tipo_cambio
#Nayeli peralta
#6B9AB024
def busqueda_lineal(lista, buscado):
    c = 0
    for i in range(len(lista)):
        c += 1
        if lista[i] == buscado:
            return i, c
    return -1, c
def busqueda_binaria(lista, buscado):
    izq, der, c = 0, len(lista) - 1, 0
    while izq <= der:
        medio = (izq + der) // 2
        c += 1
        if lista[medio] == buscado:
            return medio, c
        if lista[medio] < buscado:
            izq = medio + 1
        else:
            der = medio - 1
    return -1, c
fechas = ["2023-10-02", "2023-10-03", "2023-10-04","2023-10-05", "2023-10-06", "2023-10-09","2023-10-10", "2023-10-11", "2023-10-12","2023-10-13", "2023-10-16", "2023-10-17","2023-10-18", "2023-10-19", "2023-10-20","2023-10-23", "2023-10-24", "2023-10-25", "2023-10-26", "2023-10-27", "2023-10-30","2023-10-31"]
tasas = [36.4330, 36.4340, 36.4350, 36.4360,36.4370, 36.4400, 36.4410, 36.4420,36.4430, 36.4440, 36.4470, 36.4480,36.4490, 36.4500, 36.4510, 36.4540,36.4550, 36.4560, 36.4570, 36.4580,36.4610, 36.4620]
def main():
    while True:
        print("\n1. Consultar fechas")
        print("2. Dólares a córdobas")
        print("3. Córdobas a dólares")
        print("4. Salir")
        op = input("Opción: ")
        if op == "4":
            break
        if op not in ("1", "2", "3"):
            print("Opción inválida")
            continue
        fecha = input("Fecha AAAA-MM-DD: ")
        pl, cl = busqueda_lineal(fechas, fecha)
        pb, cb = busqueda_binaria(fechas, fecha)
        if pb == -1:
            print("Fecha no encontrada")
            print("Lineal:", cl, "Binaria:", cb)
            continue
        tasa = tasas[pb]
        print("Tipo de cambio:", tasa)
        print("Lineal:", cl, "Binaria:", cb)
        if op == "2":
            monto = float(input("Dólares: "))
            print("Córdobas:", monto * tasa)
        elif op == "3":
            monto = float(input("Córdobas: "))
            print("Dólares:", monto / tasa)
if __name__ == "__main__":
    main()