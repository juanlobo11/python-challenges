
print(f' ***Sistema de prestamo de libros ***')

tiene_membresia = input('Cuentas con credencial de estudiantes? (Si/no) ')
distancia_permitida_km = 3
distancia_usuario_km = int(input('A cuantos km vives de la biblioteca? '))

elegible_prestamo = (tiene_membresia.strip().lower() == 'si'
                     or distancia_usuario_km <= distancia_permitida_km)

print(f'Eres elegible para prestamo de libros? {elegible_prestamo}')