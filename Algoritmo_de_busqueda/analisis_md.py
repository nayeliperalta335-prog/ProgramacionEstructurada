#Analisis_md
#Nayeli peralta
#6B9AB024

#PREGUNTA 1
# esta tabla es la reprecentacion que salio al probar las facturas, se puede observar que la busqueda binaria falla en diferentes ocaciones ya que la lista no esta ordenada
# Factura buscada /  Posicion lineal /  Posicion binaria /  Comprobaciones binarias /   Resultado
# 8875               7                    7                       1                     correcto
# 4821               0                   -1                       4                     falla
# 2290               3                    3                       2                    correcto         
# 7041              11                   -1                       4                     falla
# 9010               13                   13                      3                     correcto

#La busqueda binaria fallo en tres facturas en la 4821, 7041 y en la 1180 aunque las tres estan en la lista el algoritmo no las encontro porque intenta descartar parte de la lista como si los numeros estuvieran ordenados, la posicion -1 indica que la busqueda binaria no encontro la factura 