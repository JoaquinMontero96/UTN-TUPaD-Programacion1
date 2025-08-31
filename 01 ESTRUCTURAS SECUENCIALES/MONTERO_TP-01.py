import math

#Ejercicio 1
print("Hola mundo!")

#Ejercicio 2
name = input("¿Cuál es tu nombre? ")
print(f"Hola {name}!")

#Ejercicio 3
name = input("Ingrese su nombre: ")
lastName = input("Ingrese su apellido: ")
age = input("Ingrese su edad: ")
country = input("Ingrese su país de residencia: ")
print(f"Soy {name} {lastName}, tengo {age} años y vivo en {country}")

#Ejercicio 4
radio = float(input("Ingrese el radio de un círculo: "))
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
print(f"El área del círculo es {area} y el perimetro es {perimetro}")

#Ejercicio 5
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas")

#Ejercicio 6
num = int(input("Ingrese un número entero: "))
print(f"{num} * 1 = {num*1}")
print(f"{num} * 2 = {num*2}")
print(f"{num} * 3 = {num*3}")
print(f"{num} * 4 = {num*4}")
print(f"{num} * 5 = {num*5}")
print(f"{num} * 6 = {num*6}")
print(f"{num} * 7 = {num*7}")
print(f"{num} * 8 = {num*8}")
print(f"{num} * 9 = {num*9}")

#Ejercicio 7
num1 = int(input("Ingrese un número distinto de 0: "))
num2 = int(input("Ingrese otro número distinto de 0: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} * {num2} = {multiplicacion}")
print(f"{num1} / {num2} = {division}")

#Ejercicio 8
altura = int(input("Ingrese su altura en cm: "))
peso = int(input("Ingrese su altura en kg: "))
imc = peso / (altura / 100) ** 2
print(f"Su índice de masa corporal es {imc}")

#Ejercicio 9
gradosC = float(input("Ingrese una temperatura en grados celsius (°C): "))
gradosF = 9 / 5 * gradosC + 32
print(f"El equivalente en Fahrenheit a {gradosC} °C es {gradosF} °F")

#Ejercicio 10
num1 = int(input("Ingrese un el primer número: "))
num2 = int(input("Ingrese un el segundo número: "))
num3 = int(input("Ingrese un el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los 3 números es {promedio}")