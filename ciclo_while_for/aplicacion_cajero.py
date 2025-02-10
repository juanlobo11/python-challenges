
print(f'*** Aplicacion de Cajero Automatico ***')

salir = False
saldo = 1000
while not salir:
    print('''Operaciones que puedes realizar:
    1. Consulta Saldo:
    2. Retirar
    3. Deposito
    4. Salir''')
    opcion = int(input('Escoje una opcion: '))

    if opcion == 1:
        print(f'Tu saldo actual es = {saldo}\n')
    elif opcion == 2:
        retiro = int(input('Ingrese el monto que desea retirar: '))
        if retiro <= saldo:
            saldo -= retiro
            print(f'''Su retiro fue exitoso!
        Se ha debitado de su cuenta: {retiro}
        Saldo disponible: {saldo}\n''')
        else:
            print(f'No cuentas con el saldo suficiente. Saldo actual: {saldo}\n')
    elif opcion == 3:
        deposito = int(input('Cuanto desea depositar? '))
        saldo += deposito
        print(f'Su nuevo saldo es: {saldo}\n')
    elif opcion == 4:
        print('Saliendo del cajero automatico. Hasta pronto!')
        salir = True
    else:
        print('Opcion invalida. Intenta nuevamente\n')