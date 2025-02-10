#operaor And
a, b = True, False

print(f'*** Operador AND ***')

resultado = a and b

print(f'Resultado {a} and {b}: {resultado}')

#operador or

resultado = a or b

print(f'Resultado {a} or {b}: {resultado}')


#operador not

resultado = not b
print(f'Resultado not sobre {b}: {resultado}')

#resivar si la variable es cadena vacia
nombre = 'Juan'
es_cadena_vacia = not nombre
print(f'\nLa variable no tiene ningun valor? {es_cadena_vacia}')

#revisar si la variable no tiene ningun valor
variable = None
es_variable_sin_valor = not variable
print(f'\nLa variable No tiene ningun valor asignado? {es_variable_sin_valor}')