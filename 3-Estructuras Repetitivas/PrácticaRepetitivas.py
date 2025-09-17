#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for num in range(0,101):
    print(num)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = int(input("Ingrese un número entero:"))
contador = 0

if num == 0:
    contador = 1
else:
    while num > 0:
        num //= 10
        contador += 1

print("Cantidad de dígitos:", contador)

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un número:"))
num2 = int(input("Ingrese otro número:"))
sumatoria = 0

for i in range(num1+1,num2):
    sumatoria += i

print(f"La sumatoria de los números intermedios es:  {sumatoria}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

num = int(input("Ingrese un número que no sea cero, en caso de ingresar cero, el programa se detendrá:"))
sumatoria = 0

while num != 0:
    sumatoria += num
    num = int(input("Ingrese un número que no sea cero, en caso de ingresar cero, el programa se detendrá:"))

print(f"El total acumulado es:  {sumatoria}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
num_aleatorio = random.randint(0, 9)
intentos = 0

num = int(input("Ingrese un número: "))
intentos += 1

if num == num_aleatorio:
    print("Usted acerto el número en el Primer intento!")
else:
    while num != num_aleatorio:
        num = int(input("Ingrese otro número: "))
        intentos += 1
        if num == num_aleatorio:
            print(f"Usted acerto el número en el intento {intentos}")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for num in range(100, -1, -2):
    if num % 2 == 0:
        print(num)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

num = int(input("Ingrese un número:"))
sumatoria = 0 

for i in range(0, num):
    sumatoria += i
print(f"La sumatoria es: {sumatoria}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range(0, 101):
    num = int(input("Ingrese un número positivo o negativo(El total de números permitidos es de 100)Interrumpe el programa con cero:"))
    if num == 0:    #Condición de corte mediante el ingreso del número cero
        break

    if num > 0:             #Validación de positivos
        positivos += 1
    elif num < 0:           #Validación de negativos
        negativos += 1

    if num % 2 == 0:    #Validación de pares
        pares += 1
    else:               #Validación de impares
        impares += 1

print(f"Los pares son: {pares}")
print(f"Los impares son: {impares}")
print(f"Los positivos son: {positivos}")
print(f"Los negativos son: {negativos}")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

media = 0
contador = 0
acumulador = 0

for i in range(0, 101):
    num = int(input("\nIngrese un número(El total de números permitidos es de 100)Interrrumpe el programa con cero:\n"))

    acumulador += num
    contador += 1 

    if num == 0:    #Condición de corte mediante el ingreso del número cero
        contador -= 1   #Resta uno al contador porque el cero es solo condición de corte, si se deja altera la media y no es el objetivo
        print("\nEl programa se interrumpió antes de los 100 números!\n")
        break
       
media = acumulador / contador
print(f"La media es: {media}" )

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un número: "))
invertido = 0

while num != 0:
    digito = num % 10        #Extrae el último dígito
    invertido = invertido * 10 + digito
    num = num // 10          #Elimina el último dígito

print("Número invertido:", invertido)