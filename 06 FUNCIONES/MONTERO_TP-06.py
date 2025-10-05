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

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

num = int(input("Ingrese un número entero para conocer su tabla de multiplicación: "))
tabla_multiplicar(num)