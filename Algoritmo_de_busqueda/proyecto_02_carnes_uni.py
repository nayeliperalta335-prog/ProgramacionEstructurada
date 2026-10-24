# Proyecto_02_carnes_uni
# Nayeli peralta
# 6B9AB024
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
        m = (izq + der) // 2
        c += 1
        if lista[m] == buscado:
            return m, c
        if lista[m] < buscado:
            izq = m + 1
        else:
            der = m - 1
    return -1, c
def carne_valido(carne):
    return (len(carne) == 10 and carne[:4].isdigit()
            and carne[4] == "-" and carne[5:9].isdigit()
            and carne[9] == "U")
def buscar_nombre(lista, buscado):
    c = 0
    for i in range(len(lista)):
        c += 1
        if lista[i].lower() == buscado.lower():
            return i, c
    return -1, c
def buscar_todos(lista, buscado):
    posiciones = []
    c = 0
    for i in range(len(lista)):
        c += 1
        if lista[i].lower() == buscado.lower():
            posiciones.append(i)
    return posiciones, c
carnes = []
nombres = []
carreras = []
def main():
    while True:
        print("\n1. Buscar por carné")
        print("2. Buscar por nombre")
        print("3. Listar por carrera")
        print("4. Salir")
        op = input("Opción: ")
        if op == "1":
            carne = input("Carné: ")
            if not carne_valido(carne):
                print("Carné inválido")
                continue
            pl, cl = busqueda_lineal(carnes, carne)
            pb, cb = busqueda_binaria(carnes, carne)
            if pb != -1:
                print(nombres[pb], carreras[pb])
            else:
                print("No encontrado")
            print("Lineal:", cl, "Binaria:", cb)
        elif op == "2":
            nombre = input("Nombre completo: ")
            p, c = buscar_nombre(nombres, nombre)
            if p != -1:
                print(carnes[p], carreras[p])
            else:
                print("No encontrado")
            print("Comparaciones:", c)
        elif op == "3":
            carrera = input("Carrera: ")
            posiciones, c = buscar_todos(carreras, carrera)
            for p in posiciones:
                print(carnes[p], nombres[p])
            print("Total:", len(posiciones))
            print("Comparaciones:", c)
        elif op == "4":
            break
        else:
            print("Opción inválida")
if __name__ == "__main__":
    main()