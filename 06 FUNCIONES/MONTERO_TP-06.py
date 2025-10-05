# # Ejercicio 1
# def imprimir_hola_mundo():
#     print("Hola Mundo!")

# imprimir_hola_mundo()

# #Ejercicio 2
# def saludar_usuario(nombre):
#     print(f"Hola {nombre}!")

# nombre = input("Cual es tu nombre? ")
# saludar_usuario(nombre)

# # Ejercicio 3
# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# print("Ingrese sus datos")
# nombre = input("Nombre: ")
# apellido = input("Apellido: ")
# edad = input("Edad: ")
# residencia = input("Lugar de residencia: ")

# informacion_personal(nombre, apellido, edad, residencia)

# # Ejercicio 4
# import math
# def calcular_area_circulo(radio):
#     return math.pi * radio**2

# def calcular_perimetro_circulo(radio):
#     return math.pi * 2 * radio

# radio = float(input("Ingrese el radio del círculo: "))
# area = round(calcular_area_circulo(radio), 2)
# perimetro = round(calcular_perimetro_circulo(radio), 2)

# print(f"El área del círculo es {area} y el perímetro {perimetro}")

# # Ejercicio 5
# def segundos_a_horas(segundos):
#     return round(segundos/60/60, 2)

# segundos = int(input("Cuantos segundos desea calcular en horas? "))
# print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas")

# # Ejercicio 6
# def tabla_multiplicar(numero):
#     for i in range(1, 11):
#         print(f"{numero} x {i} = {numero * i}")

# num = int(input("Ingrese un número entero para conocer su tabla de multiplicación: "))
# tabla_multiplicar(num)

# # Ejercicio 7
# def operaciones_basicas(a, b):
#     resultados = (a + b, a - b, a * b, a / b)
#     return resultados

# num1 = 7
# num2 = 5
# resultados = operaciones_basicas(num1, num2)

# print(f"{num1} + {num2} = {resultados[0]}")
# print(f"{num1} - {num2} = {resultados[1]}")
# print(f"{num1} * {num2} = {resultados[2]}")
# print(f"{num1} / {num2} = {resultados[3]}")

# # Ejercicio 8
# def calcular_imc(peso, altura):
#     return round((peso / (altura / 100) ** 2), 2)

# peso = float(input("Ingrese su peso expresado en kg: "))
# altura = float(input("Ingrese su altura expresada en cm: "))
# imc = calcular_imc(peso, altura)

# print(f"Su índice de masa corporal es {imc}")

# Ejercicio 9
def celcius_a_farenheit(temp):
    return temp * 1.8 + 32

temperatura_celsius = float(input("Ingrese una temperatura en grados celsius: "))
temperatura_farenheit = celcius_a_farenheit(temperatura_celsius)

print(f"{temperatura_celsius}°C es equivalente a {temperatura_farenheit}°F")