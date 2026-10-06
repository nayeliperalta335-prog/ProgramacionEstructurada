ruta = ("Estelí", "Managua", 148, 170.00)
origen, destino, km, pasaje = ruta
costo_km = pasaje / km
print("Ruta:", origen, "-", destino)
print("Distancia:", km, "km")
print(f"Pasaje: C$ {pasaje:.2f}")
print(f"Costo por kilómetro: C$ {costo_km:.2f}")
origen, destino = destino, origen
print("Ruta de regreso:", origen, "-", destino)