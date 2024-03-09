class PagoComida(object):
    stock_inicial = 100

    def __init__(self):
        self.stock_disponible = self.stock_inicial
        self.movimientos = []
