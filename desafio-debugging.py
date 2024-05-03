def recomendacion_planta(cuidado):
    if cuidado == "bajo":
        print("Noche Buena")
    elif cuidado == "medio":
        print("Pothos")
    elif cuidado == "alto":
        print("Orquidea")
    else:
        print("Valor no encontrado.")

recomendacion_planta("bajo")
recomendacion_planta("medio")
recomendacion_planta("alto")
