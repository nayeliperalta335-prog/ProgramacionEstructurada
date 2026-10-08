temp_managua = (31, 33, 32, 34, 30, 29, 32)
temp_esteli = (24, 26, 25, 23, 27, 25, 24)
def resumen(datos):
    minima = min(datos)
    maxima = max(datos)
    total = 0
    for temperatura in datos:
        total += temperatura
    promedio = total / len(datos)
    return minima, maxima, promedio
minima, maxima, promedio = resumen(temp_managua)
print( f"Managua -> mínima: {minima} °C, "f"máxima: {maxima} °C, " f"promedio: {promedio:.1f} °C")
minima, maxima, promedio = resumen(temp_esteli)
print( f"Estelí -> mínima: {minima} °C, "f"máxima: {maxima} °C, "f"promedio: {promedio:.1f} °C")