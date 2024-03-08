class PagoComida(object):
    stock_inicial = 100  

    def __init__(self):
        self.stock_disponible = self.stock_inicial
        self.movimientos = []

   # def pagar(self):
   #     if self.stock_disponible > 0:
   #         self.stock_disponible -= 1
   #         self.movimientos.append("Pago de comida: -1")
   #         return True  # Indica que el pago de comida fue exitoso
   #     else:
   #         return False  # Indica que no hay existencias disponibles para el pago de comida
