print('*** Sistema de Administracion de cuentas ***')

salir = False

while not salir:
    print(f'''Menu:
    1. Crear Cuenta
    2. Eliminar cuenta
    3. Salir''')
    opcion = int(input('Escoje una opcion: '))
    if opcion == 1:
        print('Creandro tu cuenta ... \n')
    elif opcion == 2:
        print('Eliminando tu cuenta ... \n')
    elif opcion == 3:
        print('Saliendo del sistema. Hasta pronto! \n')
        salir = True
    else:
        print('Opcion invalida, proporciona otra opcion \n')
else:
    print('Terminando la ejecucion del sistema...')
