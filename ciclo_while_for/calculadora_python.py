print("*** Calculadora Python ***")
salir = False
while not salir:
    print('''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir''')
    opcion = int(input('Escoje una opcion: '))
    #solicitamos ambos valores
    if 1<= opcion <= 4:  # con el valor 5 no nos pedira los valores
        valor1 = float(input('Ingresa el primer valor: '))
        valor2 = float(input('Ingresa el segundo valor: '))
    #revisamos tipo de operacion
    if opcion == 1:
        resultado = valor1 + valor2
        print(f'El resultado de la suma es: {resultado}')
    elif opcion == 2:
        resultado = valor1 - valor2
        print(f'El resultado de la resta es: {resultado}')
    elif opcion == 3:
        resultado = valor1 * valor2
        print(f'El resultado de la multiplicacion es: {resultado}\n')
    elif opcion == 4:
        resultado = valor1 / valor2
        print(f'El resultado de la division es: {resultado}\n')
    elif opcion == 5:
        print('Saliendo del programa. Hasta pronto!')
        salir = True
    else:
        print('Opcion invalida. Intenta nuevamente')
