class AlquilerBicicleta(object):
    stock_inicial = 10

    def __init__(self):
        self.stock_disponible = self.stock_inicial
        self.prestamos_realizados = 0
        self.movimientos = []

    def reservar(self):
        if self.stock_disponible > 0:
            self.stock_disponible -= 1
            self.prestamos_realizados += 1
            self.movimientos.append("Reserva de bicicleta: +1")
            return True  # Indica que la reserva fue exitosa
        else:
            return False  # Indica que no hay existencias disponibles

    def devolver(self):
        if self.prestamos_realizados > 0:
            self.stock_disponible += 1
            self.prestamos_realizados -= 1
            self.movimientos.append("Devolución de bicicleta: +1")
            return True  # Indica que la devolución fue exitosa
        else:
            return False  # Indica que no hay reservas para devolver

    def consultar_stock(self):
        return self.stock_disponible

    def consultar_prestamos(self):
        return self.prestamos_realizados
