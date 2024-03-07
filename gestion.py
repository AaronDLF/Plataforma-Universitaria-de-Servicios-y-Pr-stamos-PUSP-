class GestionRecursosServicios(object):
    def __init__(self):
        self.recursos_disponibles = {
            "Computadoras": 20,
            "Bicicletas": 10,
            "Comida": 100,
            "Materiales de papelería": 50
        }

    def mostrar_inventario(self):
        print("\nInventario Actual:")
        for recurso, cantidad in self.recursos_disponibles.items():
            print(f"{recurso}: {cantidad}")

    def agregar_recurso(self, recurso, cantidad):
        if recurso in self.recursos_disponibles:
            self.recursos_disponibles[recurso] += cantidad
            print(f"{cantidad} unidades de {recurso} fueron agregadas al inventario.")
        else:
            print("Recurso no válido.")

    def eliminar_recurso(self, recurso, cantidad):
        if recurso in self.recursos_disponibles:
            if self.recursos_disponibles[recurso] >= cantidad:
                self.recursos_disponibles[recurso] -= cantidad
                print(f"{cantidad} unidades de {recurso} fueron eliminadas del inventario.")
            else:
                print("No hay suficientes unidades disponibles para eliminar.")
        else:
            print("Recurso no válido.")