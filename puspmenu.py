

from prettytable import PrettyTable
from colorama import Fore, Style
from pyfiglet import Figlet
from alquilercomputadora import AlquilerComputadora 
from alquilerbicicleta import AlquilerBicicleta
from comida import PagoComida
from materiales import PagoMaterialesPapeleria
from gestion import GestionRecursosServicios

COSTO_ALQUILER_COMPUTADORA = 100
COSTO_RESERVA_BICICLETA = 20
COSTO_COMIDA = 50
COSTO_MATERIALES_PAPELERIA = 80

EXISTENCIAS = {
    "Computadoras": 20,
    "Bicicletas": 10,
    "Comida": 100,
    "Materiales de papelería": 50
}


class PUSPMenu(object):

    def __init__(self, usuario):
        self.usuario = usuario
        self.saldo_inicial = 5000
        self.movimientos = []
        self.alquiler_computadora = AlquilerComputadora()
        self.alquiler_bicicleta = AlquilerBicicleta()  

    def mostrar_titulo(self):
        custom_fig = Figlet(font='slant')
        titulo = custom_fig.renderText("PUSP")
        print(Fore.BLUE + titulo + Style.RESET_ALL)

    def mostrar_menu(self):
        self.mostrar_titulo()

        if self.usuario == 'admin':
            self.mostrar_menu_admin()
        elif self.usuario == 'usuario':
            self.mostrar_menu_usuario_comun()
        else:
            print("Tipo de usuario no reconocido")

    def mostrar_menu_admin(self):
        while True:
            table = PrettyTable()
            table.field_names = ["Opción", "Descripción"]
            table.add_row(["1", "Gestionar recursos y servicios"])
            table.add_row(["2", "Ver análisis de datos"])
            table.add_row(["3", "Cambiar perfil"])
            table.add_row(["4", "Cerrar sesión"])
            print(table)

            opcion_admin = input("Ingrese el número de la opción deseada: ")

            if opcion_admin == '1':
                self.ejecutar_opcion_gestion_recursos()
            elif opcion_admin == '2':
                # Agrega aquí la lógica para ver análisis de datos
                print("Función de análisis de datos en construcción.")
            elif opcion_admin == '3':
                self.cambiar_perfil()
            elif opcion_admin == '4':
                break
            else:
                print("Opción no válida. Por favor, ingrese un número válido.")

    def cambiar_perfil(self):
        nuevo_perfil = input("Ingrese el nuevo perfil ('admin' o 'usuario'): ").lower()
        if nuevo_perfil in ['admin', 'usuario']:
            self.usuario = nuevo_perfil
            print(f"Perfil cambiado a: {self.usuario}")
            self.mostrar_menu()
        else:
            print("Perfil no válido. Por favor, ingrese 'admin' o 'usuario'.")

    def ejecutar_opcion_gestion_recursos(self):
        while True:
            print("\nMenú de Gestionar Recursos y Servicios:")
            print("1. Mostrar inventario")
            print("2. Agregar recursos")
            print("3. Eliminar recursos")
            print("4. Cambiar perfil")
            print("5. Volver al menú principal")
            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == '1':
                GestionRecursosServicios.mostrar_inventario(EXISTENCIAS)
            elif opcion == '2':
                recurso = input("Ingrese el nombre del recurso a agregar: ")
                cantidad = int(input("Ingrese la cantidad a agregar: "))
                GestionRecursosServicios.agregar_recurso(EXISTENCIAS, recurso, cantidad)
            elif opcion == '3':
                recurso = input("Ingrese el nombre del recurso a eliminar: ")
                cantidad = int(input("Ingrese la cantidad a eliminar: "))
                GestionRecursosServicios.eliminar_recurso(EXISTENCIAS, recurso, cantidad)
            elif opcion == '4':
                self.cambiar_perfil()
            elif opcion == '5':
                break
            else:
                print("Opción no válida. Por favor, ingrese un número válido.")

    def mostrar_menu_usuario_comun(self):
        while True:
            table = PrettyTable()
            table.field_names = ["Opción", "Descripción"]
            table.add_row(["1", "Alquilar computadora"])
            table.add_row(["2", "Reservar bicicleta"])
            table.add_row(["3", "Pagar comida "])
            table.add_row(["4", "Pagar materiales de papeleria"])
            table.add_row(["5", "Consultar saldo"])
            table.add_row(["6", "Historial de movimientos"])
            table.add_row(["7", "Cambiar perfil"])
            table.add_row(["8", "Cerrar sesión"])
            print(table)

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == '1':
                self.alquilar_computadora()
            elif opcion == '2':
                self.reservar_bicicleta()
            elif opcion == '3':
                self.ejecutar_opcion_pagar_comida()
            elif opcion == '4':
                self.ejecutar_opcion_pagar_materiales_papeleria()
            elif opcion == '5':
                self.consultar_saldo()
            elif opcion == '6':
                self.consultar_historial_movimientos()
            elif opcion == '7':
                self.cambiar_perfil()
            elif opcion == '8':
                break
            else:
                print("Opción no válida. Por favor, ingrese un número válido.")

    def mostrar_inventario(self):
        print("\nInventario Actual:")
        for recurso, cantidad in EXISTENCIAS.items():
            print(f"{recurso}: {cantidad}")

    def agregar_recurso(self, recurso, cantidad):
        if recurso in EXISTENCIAS:
            EXISTENCIAS[recurso] += cantidad
            print(f"{cantidad} unidades de {recurso} fueron agregadas al inventario.")
        else:
            print("Recurso no válido.")

    def eliminar_recurso(self, recurso, cantidad):
        if recurso in EXISTENCIAS:
            if EXISTENCIAS[recurso] >= cantidad:
                EXISTENCIAS[recurso] -= cantidad
                print(f"{cantidad} unidades de {recurso} fueron eliminadas del inventario.")
            else:
                print("No hay suficientes unidades disponibles para eliminar.")
        else:
            print("Recurso no válido.")


    def alquilar_computadora(self):
        if EXISTENCIAS["Computadoras"] > 0:
            if self.alquiler_computadora.alquilar():
                self.movimientos.append("Alquiler de computadora: +1")
                print("Computadora alquilada con éxito.")
                opcion_devolucion = input("¿Desea devolver la computadora ahora? (Sí/No): ").lower()
                if opcion_devolucion == 'si':
                    self.devolver_computadora()
                EXISTENCIAS["Computadoras"] -= 1  # Actualiza las existencias después de alquilar
            else:
                print("¡Existencias agotadas! No se pueden realizar más préstamos de computadoras.")
        else:
            print("¡Existencias de computadoras agotadas! No se pueden realizar más préstamos.")


    def devolver_computadora(self):
        if self.alquiler_computadora.devolver():
            self.movimientos.append("Devolución de computadora: +1")
            print("Computadora devuelta con éxito.")
        else:
            print("No hay préstamos para devolver en este momento.")

    def reservar_bicicleta(self):
        if EXISTENCIAS["Bicicletas"] > 0:
            if self.alquiler_bicicleta.reservar():
                self.movimientos.append("Reserva de bicicleta: +1")
                print("Bicicleta reservada con éxito.")
                opcion_devolucion = input("¿Desea devolver la bicicleta ahora? (Sí/No): ").lower()
                if opcion_devolucion == 'si':
                    self.devolver_bicicleta()
                EXISTENCIAS["Bicicletas"] -= 1  # Actualiza las existencias después de reservar
            else:
                print("¡Existencias agotadas! No se pueden realizar más reservas de bicicletas.")
        else:
            print("¡Existencias de bicicletas agotadas! No se pueden realizar más reservas.")


    def devolver_bicicleta(self):
        if self.alquiler_bicicleta.devolver():
            self.movimientos.append("Devolución de bicicleta: +1")
            print("Bicicleta devuelta con éxito.")
        else:
            print("No hay reservas para devolver en este momento.")

    def ejecutar_opcion_pagar_comida(self, pago_comida):
        if pago_comida.pagar():
            self.saldo_inicial -= COSTO_COMIDA  # Ajusta según el costo de comida que hayas definido
            self.movimientos.extend(pago_comida.movimientos)
            print("Pago de comida realizado con éxito.")
        else:
            print("Stock insuficiente. No se puede realizar el pago de comida.")

    def ejecutar_opcion_pagar_materiales_papeleria(self, pago_materiales_papeleria):
        if pago_materiales_papeleria.pagar():
            self.saldo_inicial -= COSTO_MATERIALES_PAPELERIA  # Ajusta según el costo de materiales de papelería que hayas definido
            self.movimientos.extend(pago_materiales_papeleria.movimientos)
            print("Pago de materiales de papelería realizado con éxito.")
        else:
            print("Stock insuficiente. No se puede realizar el pago de materiales de papelería.")
    

    def consultar_historial_movimientos(self):
        print("\nHistorial de Movimientos:")
        for movimiento in self.movimientos:
            print(movimiento)
    
    def consultar_saldo(self):
        saldo_actual = self.saldo_inicial
        for movimiento in self.movimientos:
            if "Alquiler de computadora" in movimiento:
                saldo_actual -= COSTO_ALQUILER_COMPUTADORA
            elif "Devolución de computadora" in movimiento:
                saldo_actual += COSTO_ALQUILER_COMPUTADORA 
            elif "Reserva de bicicleta" in movimiento:
                saldo_actual -= COSTO_RESERVA_BICICLETA   
            elif "Devolución de bicicleta" in movimiento:
                saldo_actual += COSTO_RESERVA_BICICLETA   

        print("Saldo actual: {}".format(saldo_actual))