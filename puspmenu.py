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
    "Materiales de papelería": 50,
}


class PuspMenu(object):

    def __init__(self, usuario):
        self.iniciar_sesion()
        self.usuario = usuario
        self.saldo_inicial = 5000
        self.movimientos = []
        self.alquiler_computadora = AlquilerComputadora()
        self.alquiler_bicicleta = AlquilerBicicleta()

    def mostrar_titulo(self):
        custom_fig = Figlet(font="slant")
        titulo = custom_fig.renderText("PUSP")
        print(Fore.BLUE + titulo + Style.RESET_ALL)

    def iniciar_sesion(self):
        print("Bienvenido al sistema PUSP.")
        while True:
            usuario_input = input("Ingrese su nombre de usuario: ")
            contrasena_input = input("Ingrese su contraseña: ")

            # Verifica las credenciales
            if self.verificar_credenciales(usuario_input, contrasena_input):
                print(
                    "Inicio de sesión exitoso. ¡Bienvenido, {}!".format(
                        usuario_input
                    )
                )
                self.usuario = usuario_input
                break
            else:
                print("Credenciales incorrectas. Inténtelo de nuevo.")

    def verificar_credenciales(self, usuario, contrasena):
        # Ejemplos de credenciales para "admin" y "usuario_comun"
        credenciales_admin = {"usuario": "admin", "contrasena": "admin123"}
        credenciales_usuario_comun = {
            "usuario": "comun",
            "contrasena": "usuario123",
        }

        if (
            usuario == credenciales_admin["usuario"]
            and contrasena == credenciales_admin["contrasena"]
        ):
            return True  # Credenciales válidas para admin
        elif (
            usuario == credenciales_usuario_comun["usuario"]
            and contrasena == credenciales_usuario_comun["contrasena"]
        ):
            return True  # Credenciales válidas para usuario_comun
        else:
            return False  # Credenciales incorrectas

    def mostrar_menu(self):
        self.mostrar_titulo()

        if self.usuario == "admin":
            self.mostrar_menu_admin()
        elif self.usuario == "usuario":
            self.mostrar_menu_usuario_comun()
        else:
            print("Tipo de usuario no reconocido")

    def mostrar_menu_admin(self):
        while True:
            table = PrettyTable()
            table.field_names = ["Opción", "Descripción"]
            table.add_row(["1", "Gestionar recursos y servicios"])
            table.add_row(["2", "Cambiar perfil"])
            table.add_row(["3", "Cerrar sesión"])
            print(table)

            opcion_admin = input("Ingrese el número de la opción deseada: ")

            if opcion_admin == "1":
                self.ejecutar_opcion_gestion_recursos()
            elif opcion_admin == "2":
                self.cambiar_perfil()
            elif opcion_admin == "3":
                self.cerrar_sesion()
                break
            else:
                print("Opción no válida. Por favor, ingrese un número válido.")

    def cambiar_perfil(self):
        nuevo_perfil = input(
            "Ingrese el nuevo perfil ('admin' o 'usuario'): "
        ).lower()
        if nuevo_perfil in ["admin", "usuario"]:
            usuario_input = input("Ingrese su nombre de usuario: ")
            contrasena_input = input("Ingrese su contraseña: ")

            if self.verificar_credenciales(usuario_input, contrasena_input):
                self.usuario = nuevo_perfil
                print(f"Perfil cambiado a: {self.usuario}")
                self.mostrar_menu()
            else:
                print(
                    "Credenciales incorrectas. No se pudo cambiar el perfil."
                )
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

            if opcion == "1":
                GestionRecursosServicios.mostrar_inventario(EXISTENCIAS)
            elif opcion == "2":
                recurso = input("Ingrese el nombre del recurso a agregar: ")
                cantidad = int(input("Ingrese la cantidad a agregar: "))
                GestionRecursosServicios.agregar_recurso(
                    EXISTENCIAS, recurso, cantidad
                )
            elif opcion == "3":
                recurso = input("Ingrese el nombre del recurso a eliminar: ")
                cantidad = int(input("Ingrese la cantidad a eliminar: "))
                GestionRecursosServicios.eliminar_recurso(
                    EXISTENCIAS, recurso, cantidad
                )
            elif opcion == "4":
                self.cambiar_perfil()
            elif opcion == "5":
                break
            else:
                print("Opción no válida. Por favor, ingrese un número válido.")

    def mostrar_menu_usuario_comun(self):
        while True:
            table = PrettyTable()
            table.field_names = ["Opción", "Descripción", "Costo"]
            table.add_row(
                ["1", "Alquilar computadora", f"${COSTO_ALQUILER_COMPUTADORA}"]
            )
            table.add_row(
                ["2", "Reservar bicicleta", f"${COSTO_RESERVA_BICICLETA}"]
            )
            table.add_row(["3", "Pagar comida", f"${COSTO_COMIDA}"])
            table.add_row(
                [
                    "4",
                    "Pagar materiales de papeleria",
                    f"${COSTO_MATERIALES_PAPELERIA}",
                ]
            )
            table.add_row(["5", "Consultar saldo", "-"])
            table.add_row(["6", "Historial de movimientos", "-"])
            table.add_row(["7", "Cambiar perfil", "-"])
            table.add_row(["8", "Cerrar sesión", "-"])
            print(table)

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self.alquilar_computadora()
            elif opcion == "2":
                self.reservar_bicicleta()
            elif opcion == "3":
                self.ejecutar_opcion_pagar_comida()
            elif opcion == "4":
                self.ejecutar_opcion_pagar_materiales_papeleria()
            elif opcion == "5":
                self.consultar_saldo()
            elif opcion == "6":
                self.consultar_historial_movimientos()
            elif opcion == "7":
                self.cambiar_perfil()
            elif opcion == "8":
                self.cerrar_sesion()
                break
            else:
                print("Opción no válida. Por favor, ingrese un número válido.")

    def cerrar_sesion(self):
        print("Sesión cerrada. ¡Hasta luego!")
        exit()  # Sale del programa después de cerrar sesión

    def mostrar_inventario(self):
        print("\nInventario Actual:")
        for recurso, cantidad in EXISTENCIAS.items():
            print(f"{recurso}: {cantidad}")

    def agregar_recurso(self, recurso, cantidad):
        if recurso in EXISTENCIAS:
            EXISTENCIAS[recurso] += cantidad
            print(
                f"{cantidad} unidades de {recurso} fueron agregadas al inventario."
            )
        else:
            print("Recurso no válido.")

    def eliminar_recurso(self, recurso, cantidad):
        if recurso in EXISTENCIAS:
            if EXISTENCIAS[recurso] >= cantidad:
                EXISTENCIAS[recurso] -= cantidad
                print(
                    f"{cantidad} unidades de {recurso} fueron eliminadas del inventario."
                )
            else:
                print("No hay suficientes unidades disponibles para eliminar.")
        else:
            print("Recurso no válido.")

    def alquilar_computadora(self):
        if EXISTENCIAS["Computadoras"] > 0:
            if self.alquiler_computadora.alquilar():
                self.movimientos.append("Alquiler de computadora: +1")
                print("Computadora alquilada con éxito.")
                EXISTENCIAS[
                    "Computadoras"
                ] -= 1  # Actualiza las existencias después de alquilar
                self.verificar_devolucion_existencias_cero("Computadoras")
            else:
                print(
                    "¡Existencias agotadas! No se pueden realizar más préstamos de computadoras."
                )
        else:
            print(
                "¡Existencias de computadoras agotadas! No se pueden realizar más préstamos."
            )

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
                EXISTENCIAS[
                    "Bicicletas"
                ] -= 1  # Actualiza las existencias después de reservar
                self.verificar_devolucion_existencias_cero("Bicicletas")
            else:
                print(
                    "¡Existencias agotadas! No se pueden realizar más reservas de bicicletas."
                )
        else:
            print(
                "¡Existencias de bicicletas agotadas! No se pueden realizar más reservas."
            )

    def devolver_bicicleta(self):
        if self.alquiler_bicicleta.devolver():
            self.movimientos.append("Devolución de bicicleta: +1")
            print("Bicicleta devuelta con éxito.")
        else:
            print("No hay reservas para devolver en este momento.")

    def verificar_devolucion_existencias_cero(self, tipo_recurso):
        if EXISTENCIAS[tipo_recurso] == 0:
            opcion_devolucion = input(
                f"Las existencias de {tipo_recurso} llegaron a cero. ¿Desea hacer una devolución? (Sí/No): "
            ).lower()
            if opcion_devolucion == "si":
                if tipo_recurso == "Computadoras":
                    self.devolver_computadora()
                elif tipo_recurso == "Bicicletas":
                    self.devolver_bicicleta()
            else:
                self.mostrar_alerta_devolucion_negada(tipo_recurso)
                opcion_devolucion = input(
                    f"Las existencias de {tipo_recurso} llegaron a cero. ¿Desea hacer una devolución? (Sí/No): "
                ).lower()

    def mostrar_alerta_devolucion_negada(self, tipo_recurso):
        print(f"¡Alerta! No se realizó la devolución de {tipo_recurso}.")

    def ejecutar_opcion_pagar_comida(self):
        if EXISTENCIAS["Comida"] > 0:
            cantidad_comida = int(
                input("Ingrese la cantidad de comida a comprar: ")
            )
            if cantidad_comida <= EXISTENCIAS["Comida"]:
                self.saldo_inicial -= COSTO_COMIDA * cantidad_comida
                self.movimientos.append(
                    f"Compra de comida: +{cantidad_comida}"
                )
                print(
                    f"Compra de comida realizada con éxito. Se compraron {cantidad_comida} unidades."
                )
                EXISTENCIAS[
                    "Comida"
                ] -= cantidad_comida  # Actualiza las existencias después de comprar
            else:
                print(
                    "Stock insuficiente. No se puede realizar la compra de comida."
                )
        else:
            print(
                "¡Existencias de comida agotadas! No se pueden realizar más compras."
            )

    def ejecutar_opcion_pagar_materiales_papeleria(self):
        if EXISTENCIAS["Materiales de papelería"] > 0:
            cantidad_materiales = int(
                input(
                    "Ingrese la cantidad de materiales de papelería a comprar: "
                )
            )
            if cantidad_materiales <= EXISTENCIAS["Materiales de papelería"]:
                self.saldo_inicial -= (
                    COSTO_MATERIALES_PAPELERIA * cantidad_materiales
                )
                self.movimientos.append(
                    f"Compra de materiales de papelería: +{cantidad_materiales}"
                )
                print(
                    f"Compra de materiales de papelería realizada con éxito. Se compraron {cantidad_materiales} unidades."
                )
                EXISTENCIAS[
                    "Materiales de papelería"
                ] -= cantidad_materiales  # Actualiza las existencias después de comprar
            else:
                print(
                    "Stock insuficiente. No se puede realizar la compra de materiales de papelería."
                )
        else:
            print(
                "¡Existencias de materiales de papelería agotadas! No se pueden realizar más compras."
            )

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


if __name__ == "__main__":
    usuario_inicial = input(
        "Ingrese su tipo de usuario (admin/usuario) **Debe digitar cualquiera de las 2 opciones dadas en los parentesis** "
    )
    puspmenu = PUSPMenu(usuario_inicial)
    puspmenu.mostrar_menu()
