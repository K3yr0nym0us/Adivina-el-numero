#pregunta el nombre al usuario
#nombre tienes que pensar en un numero entre el 1 y el 100 tienes 8 intentos para adivinarlo

#si el numero es menor a 1 o superior a 100 entonces
#numero no permitido

#si el numero es menor incorrecto es menor

#si el numero es mayor incorrecto es mayor

#si el usario acierta ganaste usaste tal intentos

#si no acierta repetir hasta agotar 8 intentos o ganar

from os import system
from random import randint

intentos = 8
numero_random = randint(1,101)

print("Bienvenido al juego Adivina el numero\n")
nombre_usuario = input("Ingresa tu nombre: ")
system("cls")
print(f"\nBien {nombre_usuario} este es el juego:\n")
print("Estoy pensando en un numero entre el 1 y el 100\nPuedes adivinarlo?\n" )
    
while intentos > 0:
    print(f"Tienes {intentos} intentos para adivinar")
    numero_usuario = int(input())
    numero_final = (intentos - 8) * -1
    if numero_usuario not in range(1,101):
        system("cls")
        print("Ingresa un numero valido!")
        continue
    elif numero_usuario > numero_random:
        intentos -= 1
        system("cls")
        print("El numero ingresado es mayor al que estoy pensando\n")
        continue
    elif numero_usuario < numero_random:
        intentos -= 1
        system("cls")
        print("El numero ingresado es menor al que estoy pensando\n")
        continue
    elif numero_usuario == numero_random:
        system("cls")
        print(f"\nFelicitaciones Ganaste!\nEl numero era {numero_random}\nLo lograste en {numero_final} intentos")
        system("timeout /t 5 > nul")
        break
else:
    system("cls")
    print(f"Te quedaste sin intentos\nEl numero era {numero_random}\nFin del juego")
    system("timeout /t 5 > nul")