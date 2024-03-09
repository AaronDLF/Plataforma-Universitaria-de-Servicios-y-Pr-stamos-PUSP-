class PagoMaterialesPapeleria(object):
    stock_inicial = 50

    def __init__(self):
        self.stock_disponible = self.stock_inicial
        self.movimientos = []
