print('*** Creacion de Password ***')

salir = False
while not salir:
    contrasena = input("Introduce tu password de al menos 6 caracteres: ")
    if len(contrasena) < 6:
        print('Password invalido, intenta de nuevo \n')
    else:
        print('Password Valido')
        salir = True
else:
    print("Saliendo del sistema...")


#while len(contrasena) < 6
 #   print('El password no cumple')
  #  contrasena = input('Ingresa un nuevo valor de password: ')
#else:
    #print('Password valido')