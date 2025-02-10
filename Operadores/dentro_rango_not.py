#REvisar si la variable esta dentro de 1 y 10

dato = int(input('Proporciona un dato entero: '))

#esta dentro de rango
esta_dentro_rango = 1 <= dato <= 10
print(f'Variable esta dentro de rango (entre 1 y 10)?: {esta_dentro_rango}')

#fuera de rango
esta_fuera_rango = dato < 1 or dato > 10
#alternativa: not(1<= dato <=10)
print(f'Variable esta fuera de rango (entre 1 y 10)?: {esta_fuera_rango}')
