estudiantes = ("Ana","Luis","Carla","José","Marta")
notas_grupo = (78, 92, 85, 66, 95)
ranking = zip(notas_grupo, estudiantes)
ranking_ordenado = sorted(ranking, reverse=True)
for posicion, (nota, estudiante) in enumerate(ranking_ordenado, start=1):
    print(f"{posicion}. {estudiante} - {nota}")