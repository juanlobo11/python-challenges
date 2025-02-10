print(f'*** Sistema Autenticacion ***')


usuario, password = 'juan', '123'

ingresa_usuario = input('Cual es tu usuario? ')
ingresa_passw = input('Cual es tu password? ')

dato_correcto = (ingresa_usuario == usuario
                 and ingresa_passw.strip() == password)

print(f'Datos correctos? {dato_correcto}')