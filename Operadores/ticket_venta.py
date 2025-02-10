print(f'*** Generacion ticket venta ***')

precio_leche = float(input('Precio Leche: '))
precio_pan = float(input('Precio pan: '))
precio_lechuga = float(input('Precio lechuga: '))
precio_platanos = float(input('Precio platano: '))

#subtotal
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

#descuento
tiene_descuento = int(input('Diga el descuento otorgado (%): '))

descuento = (subtotal * tiene_descuento)/100

subtotal_con_descuento = subtotal - descuento
#impuestos 19%
impuesto = subtotal * 0.19

#total compra (con impuestos)
costo_total_compra = subtotal_con_descuento + impuesto
print(f'''
Subtotal: ${subtotal:.3f}
Descuento aplicado = ${descuento:.3f}
subtotal con descuento: ${subtotal_con_descuento:.3f}
Impuesto (19%): ${impuesto:.3f}
Costo total compra: ${costo_total_compra:.3f}''')