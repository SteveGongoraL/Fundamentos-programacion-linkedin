# Clase
class Invitado:
    "Clase comun para todos los invitados"

    # Metodo constructor
    def __init__(self, nombre, ticket):
        # Atributos
        self.nombre = nombre
        self.ticket = ticket
    
    def mostrar_invitado(self):
        print(f"El nombre es: {self.nombre}. El numero de ticket es: {self.ticket}")
    
    def tickets_totales(self):
        self.ticket += 1
        print(f"El total de tickets que se han recibido son: {self.ticket}")

# Objeto
invitado_1 = Invitado("Jesus", 3)
invitado_2 = Invitado("Miguel", 5)

# Metodos
invitado_1.mostrar_invitado()
invitado_1.tickets_totales()

invitado_2.mostrar_invitado()
invitado_2.tickets_totales()
