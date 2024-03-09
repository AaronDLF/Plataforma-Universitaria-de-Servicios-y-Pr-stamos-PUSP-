from puspmenu import PUSPMenu

from prettytable import PrettyTable

# Credenciales de prueba para "admin" y "usuario_comun"
credenciales_admin = {"usuario": "admin", "contrasena": "admin123"}
credenciales_usuario_comun = {"usuario": "comun", "contrasena": "usuario123"}

# Mostrar la tabla de credenciales de prueba
credenciales_table = PrettyTable()
credenciales_table.field_names = ["Tipo de Usuario", "Nombre de Usuario", "Contraseña"]
credenciales_table.add_row(["Admin", credenciales_admin["usuario"], credenciales_admin["contrasena"]])
credenciales_table.add_row(["Usuario Común", credenciales_usuario_comun["usuario"], credenciales_usuario_comun["contrasena"]])
print("Credenciales de Prueba:")
print(credenciales_table)
print("Se requiere que ingrese algunas de las credenciales indicadas para ejecutar el código")

# Solicitar al usuario que ingrese su tipo de cliente

tipo_usuario = input("Por favor, ingrese su tipo de cliente (admin/usuario): ").lower()

# Verificar y mostrar el menú correspondiente
if tipo_usuario in ['admin', 'usuario']:
    menu_pusp = PUSPMenu(tipo_usuario)
    menu_pusp.mostrar_menu()
else:
    print("Tipo de usuario no válido.")
