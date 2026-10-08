menu = ("Gallo pinto","Nacatamal","Quesillo")
precios = (60.00, 90.00, 70.00)
# Esta línea produce TypeError porque las tuplas son inmutables:
# precios[0] = 65.00
print("Precios originales:", precios)
precios_lista = list(precios)
for i in range(len(precios_lista)):
    precios_lista[i] = round(precios_lista[i] * 1.10, 2)
nuevos_precios = tuple(precios_lista)
menu = menu + ("Vigorón",)
print("Precios con aumento:", nuevos_precios)
print("Menú ampliado:", menu)
print("Cantidad de platos:", len(menu))
print("¿nuevos_precios es tupla?:", type(nuevos_precios) == tuple)