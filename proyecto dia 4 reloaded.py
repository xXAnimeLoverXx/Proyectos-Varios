nombre = input('Saludos jugador, indica tu nombre: ')
input(f'Bien {nombre} el juego es, "Adivina el numero"')
input('Es un numero entre (1-30)')
input('Posees 8 intentos para adivinar, estas listo? ')
from random import *
intentos = 0
numero = randint(0,31)
while intentos < 8:
    intentos+=1
    respuesta = int(input('Cual es el numero? '))
    if respuesta > numero:
        print('El numero secreto es MENOR')
    if respuesta < numero:
        print('El numero secreto es MAYOR')
    if respuesta == numero:
        print('Bravo, ese es el numero!')
        break

print(f'Has gastado {intentos} intentos')
if intentos > 5:
    print('Casi palmas')
elif intentos <= 5:
    print('Lo has sacado rapido!')

