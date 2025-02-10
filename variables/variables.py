# Variables en Python
from traceback import print_tb
from xml.dom.minidom import ProcessingInstruction

#declaracion de Variables. Inicializacion de variables

edad = 28
altura = 1.65
pais = 'Colombia'


#Accedemos a la variable
print('Valores Iniciales: ')
print("Edad:", edad)
print('Altura:', altura)
print('pais:', pais)


#Lets modify the value of a variable.

edad = 30
altura = 1.68

#Accedemos a la variable
print('Valores secundarios: ')
print("Edad:", edad)
print('Altura:', altura)
print('pais:', pais)

#The type of the variable is dynamic.

edad = 'treinta'
print(edad)

#If we want to accede to a variable don't created, it shows error
telefono = '3013346335'
print('Telefono: ', telefono)

help()







