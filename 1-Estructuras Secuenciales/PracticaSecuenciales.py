#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = str(input("Ingrese su nombre:"))
print("Hola ", nombre)

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
edad = str(input("Ingrese su edad: "))
pais = str(input("Ingrese su Pais de residencia: "))
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}.")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

radio = float(input("Ingrese el radio de un circulo: "))
perimetro = float(input("Ingrese el perimetro de un circulo: "))
pi = 3.14
area = pi*(radio**2)
perimetro = 2*pi*radio
print(f"El area es {area}, y el perimetro es {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundos = float(input("Ingrese cantidad de segundos y le imprimo a cuantas horas equivale: "))
segundosEnUnaHora = 3600
cantidadHoras = segundos/segundosEnUnaHora
print(f"Los segundos ingresados equivalen a {cantidadHoras} horas.")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

num = int(input("Ingrese un numero y se imprimira por pantalla su tabla de multiplicar: "))
print("2x1:",num*1)
print("2x2:",num*2)
print("2x3:",num*3)
print("2x4:",num*4)
print("2x5:",num*5)
print("2x6:",num*6)
print("2x7:",num*7)
print("2x8:",num*8)
print("2x9:",num*9)
print("2x10:",num*10)

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese un numero entero distinto de cero: "))
num2 = int(input("Ingrese otro numero entero distinto de cero: "))
suma = num1+num2
resta = num1-num2
multiplicacion = num1*num2
division = num1/num2
print(f"La suma de los numeros ingresados es {suma}, la resta es {resta}, la multiplicacion es {multiplicacion} y la division es {division}.")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo: IMC=peso en kg/(altura en Metros)2

altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc = peso/(altura)**2
print(f"Su IMC es: {imc}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5.𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

gradosCelsius = float(input("Ingrese la temperatura en grados celsius: "))
gradosFahrenheit = 9/5*gradosCelsius+32
print(f"Su equivalente en grados fahrenheit son:{gradosFahrenheit}.")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
promedio = (num1+num2+num3)/3
print(f"El promedio de los numeros ingresados es:{promedio}")