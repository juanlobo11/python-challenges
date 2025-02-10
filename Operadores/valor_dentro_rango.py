print(f'*** Valor dentro de rango ***')

VALOR_MINIMO = 0
VALOR_MAXIMO = 5

valor_usuario = int(input(f'Ingrese un valor entre '
                          f'{VALOR_MINIMO} y {VALOR_MAXIMO}: '))

esta_dentro_rango = VALOR_MAXIMO >= valor_usuario >= VALOR_MINIMO
print(f'Valor dentro de rango? {esta_dentro_rango} ')