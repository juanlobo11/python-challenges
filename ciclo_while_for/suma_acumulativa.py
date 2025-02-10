print('*** Suma acumulativa ***')

#sumar los primeros 5 numeros
MAXIMO = 5
numero = 1
acumulador_suma = 0

#empezamos a iterar

while numero <= MAXIMO:
    # imprimir las sumas acumuladas
    print(f'(acumulador suma + numero) -> {acumulador_suma} + {numero}')

    acumulador_suma += numero
    numero += 1

    #imprimir resultado de la suma parcial
    print(f'Suma parcial acumulada: {acumulador_suma}\n')
print("Resultado de la suma acumulada: {}".format(acumulador_suma))


#imprimir las sumas acumuladas