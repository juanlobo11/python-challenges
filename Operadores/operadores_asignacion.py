cadena1 = ("Hola Mundo")

print(f'La cadena es {cadena1}')


#asignacion multiple
x, y, z = 5, 'Hola', -9.15

print(f'Valor de x = {x}, y = {y}, z = {z}')

#asignacion encadenada

a = b = c = 10
print(f'Valor de a = {a}, b = {b}, c = {c}')

#intercambio de valores de una variable

x, y = 5, 10
print(f'Valores iniciales x = {x}, y = {y}')
x, y = y, x
print(f'Valores invertidos x = {x}, y = {y}')

nombre, apellido = input("Ingresa tu nombre y apellido separados por coma: ").split(',')
print(f'Nombre: {nombre}, apellido: {apellido}')


