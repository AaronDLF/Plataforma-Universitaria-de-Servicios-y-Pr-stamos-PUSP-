from puspmenu import PUSPMenu

# Solicitar al usuario que ingrese su tipo de cliente
tipo_usuario = input("Por favor, ingrese su tipo de cliente (admin/usuario): ").lower()

# Verificar y mostrar el menú correspondiente
if tipo_usuario in ['admin', 'usuario']:
    menu_pusp = PUSPMenu(tipo_usuario)
    menu_pusp.mostrar_menu()
else:
    print("Tipo de usuario no válido.")
