class GestionRecursosServicios(object):

    @staticmethod
    def mostrar_inventario(existencias):
        print("\nInventario Actual:")
        for recurso, cantidad in existencias.items():
            print(f"{recurso}: {cantidad}")

    @staticmethod
    def agregar_recurso(existencias, recurso, cantidad):
        if recurso in existencias:
            existencias[recurso] += cantidad
            print(f"{cantidad} unidades de {recurso} fueron agregadas al inventario.")
        else:
            print("Recurso no válido.")

    @staticmethod
    def eliminar_recurso(existencias, recurso, cantidad):
        if recurso in existencias:
            if existencias[recurso] >= cantidad:
                existencias[recurso] -= cantidad
                print(f"{cantidad} unidades de {recurso} fueron eliminadas del inventario.")
            else:
                print("No hay suficientes unidades disponibles para eliminar.")
        else:
            print("Recurso no válido.")
