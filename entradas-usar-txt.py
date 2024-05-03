archivo_valores = open("archivos/valores.txt", "rt")
archivo_valores_totales = open("archivos/valores-totales.txt", "wt")
acumulado = 0

print("Procesando entrada......")

for linea in archivo_valores:
    acumulado += int(linea)
    print(linea.rsplit(), file=archivo_valores_totales)

print(f"\nTotal: {acumulado}", file=archivo_valores_totales)
archivo_valores_totales.close()
print("Ejecución finalizada.")
