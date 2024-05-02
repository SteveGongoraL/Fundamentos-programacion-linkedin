primer_nombre = "jesus"
segundo_nombre = "manuel"
texto_prueba = "Hola Como Estas"

# Cambiando a que la primera letra sea mayuscula.
primer_nombre_cap = primer_nombre.capitalize()
segundo_nombre_cap = segundo_nombre.capitalize()
# Sustracion de texto.
texto_ubicacion = texto_prueba.find("Como") #Extrae el indice de la palabra.
texto_extraido = texto_prueba[texto_ubicacion:] #Se pone el indice desde donde comienza.

# Imprimeindo valores.
print(primer_nombre_cap)
print(segundo_nombre_cap)
print(texto_extraido)
