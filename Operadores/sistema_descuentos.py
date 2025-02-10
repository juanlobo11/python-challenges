print( '*** Sistema de descuentos VIP ***')

no_productos_descuento = 10

no_productos_cliente = int(input('Indique cuantos productos compró: '))
tiene_membresia = input('Tiene membresia? (si/no) ')

es_elegible_descuento = (no_productos_cliente >= no_productos_descuento
                         and tiene_membresia.strip().lower() == 'si' )

print(f'Tienes acceso al descuento VIP? {es_elegible_descuento}')

